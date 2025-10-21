
import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Navigate to the local game file
        await page.goto(f"file://{os.getcwd()}/index.html")

        # Wait for the start screen to be ready and click the start button
        await page.wait_for_selector("#action-button", state="visible")
        await page.click("#action-button")

        # Wait for the game's HUD to become visible by waiting for the overlay to disappear
        await page.wait_for_selector("#message-overlay", state="hidden")

        # Wait for 5 seconds to allow game elements to appear and interactions to happen
        await asyncio.sleep(5)

        # Take a screenshot to verify the in-game state
        await page.screenshot(path="jules-scratch/verification/verification.png")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
