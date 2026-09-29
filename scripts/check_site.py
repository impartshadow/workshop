"""Browser smoke check. Requires Playwright and its Chromium browser installed.

Usage: python3 scripts/check_site.py http://localhost:8000/ /tmp/workshop-check
Also accepts the live Pages URL. Downloads are compared to this checkout.
"""
import argparse
from pathlib import Path
from urllib.parse import urljoin
from playwright.sync_api import sync_playwright, expect

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        for width, height in [(1440, 1000), (390, 844)]:
            context = browser.new_context(viewport={"width": width, "height": height},
                                          permissions=["clipboard-read", "clipboard-write"])
            page = context.new_page()
            errors = []
            page.on("pageerror", lambda error: errors.append(str(error)))
            response = page.goto(args.url, wait_until="networkidle")
            assert response and response.status == 200
            assert page.locator("h1").is_visible()
            assert page.evaluate("document.documentElement.scrollWidth <= innerWidth"), "Horizontal overflow"
            page.get_by_role("link", name="Find a project").click()
            assert page.url.endswith("#projects")
            page.locator("#copy").click()
            expect(page.locator("#copy-status")).to_contain_text("Copied")
            assert "Help me contribute" in page.evaluate("navigator.clipboard.readText()")
            assert page.locator("#available-work article").count() == 2
            for project in ("biology-map", "collaboration"):
                with page.expect_download() as pending:
                    page.locator(f'a[download][href="downloads/{project}.zip"]').click()
                download = pending.value
                target = args.output / f"{width}-{project}.zip"
                download.save_as(target)
                assert target.read_bytes() == (ROOT / f"downloads/{project}.zip").read_bytes(), "Deployed packet differs"
            for href in page.locator('a[href^="#"]').evaluate_all("els => els.map(e => e.getAttribute('href'))"):
                assert page.locator(href).count(), f"Missing section {href}"
            for asset in ("app.js", "style.css"):
                assert context.request.get(urljoin(args.url, asset)).status == 200
            assert not errors, errors
            page.screenshot(path=str(args.output / f"site-{width}.png"), full_page=True)
            print(f"PASS {width}px: layout, navigation, clipboard, both exact downloads, sections, assets, no script errors")
            context.close()
        browser.close()


if __name__ == "__main__":
    main()
