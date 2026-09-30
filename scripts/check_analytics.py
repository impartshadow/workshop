"""Browser checks with a fake receiving service. Does not claim live collection."""
from pathlib import Path
from playwright.sync_api import sync_playwright, expect

ROOT = Path(__file__).resolve().parents[1]
URL = 'http://127.0.0.1:8047/'
SCRIPT = """window.received=[];window.goatcounter.count=function(v){
window.received.push({...window.goatcounter,...v});};"""
with sync_playwright() as p:
    browser = p.chromium.launch()
    for mode in ('disabled', 'enabled', 'optout', 'dnt', 'gpc', 'blocked'):
        context = browser.new_context(permissions=['clipboard-read', 'clipboard-write'])
        if mode == 'dnt':
            context.add_init_script("Object.defineProperty(navigator,'doNotTrack',{get:()=> '1'});")
        if mode == 'gpc':
            context.add_init_script("Object.defineProperty(navigator,'globalPrivacyControl',{get:()=> true});")
        context.add_init_script("Object.defineProperty(navigator, 'clipboard', {value: {writeText: async () => {}}});")
        page = context.new_page()
        requests = []
        page.on('request', lambda r: requests.append(r.url))
        html = (ROOT / 'index.html').read_text().replace('https://impartshadow-workshop.goatcounter.com/count', '')
        if mode != 'disabled':
            html = html.replace('name="workshop-analytics" content=""',
                                'name="workshop-analytics" content="https://test.goatcounter.com/count"')
        page.route('http://127.0.0.1:8047/?*', lambda r: r.fulfill(body=html, content_type='text/html'))
        page.route('https://gc.zgo.at/count.js',
                   lambda r: r.abort() if mode == 'blocked' else r.fulfill(body=SCRIPT, content_type='text/javascript'))
        suffix = '?analytics=off' if mode == 'optout' else '?utm_source=moltbook&private=never-send#private-fragment'
        page.goto(URL + suffix)
        page.locator('#copy').click()
        expect(page.locator('#copy-status')).to_contain_text('Copied')
        page.get_by_role('link', name='Find a project').click()
        if mode == 'enabled':
            page.locator('a[download]').first.click()
            received = page.evaluate('window.received')
            assert [r['path'] for r in received] == ['/workshop/', 'copy-prompt', 'view-projects', 'download-biology-map']
            assert all(r['referrer'] == 'moltbook' for r in received)
            assert 'never-send' not in str(received) and 'private-fragment' not in str(received)
            # A clipboard failure must not count a successful copy.
            page.evaluate("() => { navigator.clipboard.writeText=async()=>{throw Error('denied')}; }")
            page.locator('#copy').click()
            expect(page.locator('#copy-status')).to_contain_text('Prompt selected')
            assert len(page.evaluate('window.received')) == 4
        elif mode != 'blocked':
            assert not any('gc.zgo.at' in r or 'goatcounter.com' in r for r in requests)
        print('PASS', mode)
        context.close()
    browser.close()
print('Local fake collector only; dashboard receipt still required after activation.')
