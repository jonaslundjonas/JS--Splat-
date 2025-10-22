import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Construct the file path to index.html
        # The script is in jules-scratch/verification, so we need to go up two levels
        file_path = "file://" + os.path.abspath("index.html")
        print(f"Navigating to: {file_path}")

        await page.goto(file_path)

        # Wait for the "Start Game" button to be visible and click it
        await page.wait_for_selector("#action-button", state="visible")
        await page.click("#action-button")

        # Wait for the game to load by checking for the message overlay to be hidden
        await page.wait_for_selector("#message-overlay", state="hidden")

        # Give the game a moment to render the enemies
        await page.wait_for_timeout(1000)

        # Create the directory if it doesn't exist
        os.makedirs("jules-scratch/verification", exist_ok=True)

        await page.screenshot(path="jules-scratch/verification/verification.png")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
