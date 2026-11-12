from app.config import settings

async def inspect_page(url: str):
    if not settings.allow_browser_automation:
        raise RuntimeError("Browser automation disabled. Set ALLOW_BROWSER_AUTOMATION=true.")
    try:
        from playwright.async_api import async_playwright
    except ImportError as exc:
        raise RuntimeError("Install requirements-browser.txt and Playwright browsers.") from exc
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url, wait_until="domcontentloaded", timeout=20000)
        result = {"url": page.url, "title": await page.title(),
                  "text": (await page.locator("body").inner_text())[:12000]}
        await browser.close()
        return result
