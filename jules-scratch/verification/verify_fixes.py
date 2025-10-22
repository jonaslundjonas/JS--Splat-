import asyncio
import os
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Get the absolute path to the HTML file
        file_path = os.path.abspath("index.html")

        # Navigate to the local HTML file
        await page.goto(f"file://{file_path}")

        # Wait for the main title to be visible, indicating the page is loaded
        await expect(page.locator("#main-title")).to_be_visible(timeout=10000)

        # Click the start button
        await page.click("#action-button")

        # Wait for the game to start by checking for the absence of the message overlay
        await expect(page.locator("#message-overlay")).to_be_hidden(timeout=10000)

        # Give the game a moment to render the first frame
        await page.wait_for_timeout(1000)

        # Take a screenshot
        await page.screenshot(path="jules-scratch/verification/verification.png")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
