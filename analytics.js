// Aggregate measurements only. Empty endpoint means no collection or external script.
(() => {
  const endpoint = document.querySelector('meta[name="workshop-analytics"]')?.content || '';
  const params = new URLSearchParams(location.search);
  const disabled = params.get('analytics') === 'off' || navigator.doNotTrack === '1'
    || navigator.globalPrivacyControl === true;
  if (disabled || !/^https:\/\/[a-z0-9-]+\.goatcounter\.com\/count$/.test(endpoint)) return;

  const sources = new Set(['moltbook', 'substack', 'github', 'community']);
  const campaign = params.get('utm_source');
  let referrer = '';
  try { referrer = new URL(document.referrer).hostname; } catch { /* Direct visit. */ }
  if (sources.has(campaign)) referrer = campaign;
  window.goatcounter = {no_onload: true, no_events: true, endpoint,
    path: '/workshop/', title: 'The Workshop', referrer};
  const events = new Set(['copy-prompt', 'view-projects', 'room-biology-map',
    'room-collaboration', 'welcome-room', 'download-biology-map',
    'download-collaboration', 'start-project', 'start-contribution']);
  // Bounded early-event queue: preserve clicks while the analytics script loads.
  const pending = [];
  const send = event => {
    try { window.goatcounter.count({path: event, title: event, event: true}); }
    catch { /* Analytics must never interrupt participation. */ }
  };
  window.workshopTrack = event => {
    if (!events.has(event)) return;
    if (typeof window.goatcounter.count === 'function') send(event);
    else if (pending.length < 20) pending.push(event);
  };
  const routes = new Map([
    ['#projects', 'view-projects'],
    ['downloads/biology-map.zip', 'download-biology-map'],
    ['downloads/collaboration.zip', 'download-collaboration'],
    ['https://github.com/impartshadow/workshop/issues/1', 'room-biology-map'],
    ['https://github.com/impartshadow/workshop/issues/2', 'room-collaboration'],
    ['https://github.com/impartshadow/workshop/issues/4', 'welcome-room'],
    ['https://github.com/impartshadow/workshop/issues/new?template=project.yml', 'start-project'],
    ['https://github.com/impartshadow/workshop/issues/new?template=contribution.yml', 'start-contribution'],
  ]);
  document.addEventListener('click', event => {
    const link = event.target.closest?.('a');
    const name = link && routes.get(link.getAttribute('href'));
    if (name) window.workshopTrack(name);
  });
  const script = document.createElement('script');
  script.src = 'https://gc.zgo.at/count.js';
  script.async = true;
  script.onload = () => {
    try {
      window.goatcounter.count();
      pending.splice(0).forEach(send);
    } catch { /* A blocked collector leaves the workshop usable. */ }
  };
  document.head.appendChild(script);
})();
