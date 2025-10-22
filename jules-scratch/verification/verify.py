
import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Construct the full path to the HTML file
        # The script is in jules-scratch/verification, the HTML is at the root
        html_file_path = "file://" + os.path.abspath("index.html")
        print(f"Loading page: {html_file_path}")

        await page.goto(html_file_path)

        # Wait for the game to be potentially ready (e.g., waiting for assets to load)
        await page.wait_for_timeout(2000)

        # Click the start button to begin the game
        print("Clicking 'Start Game' button...")
        await page.click('#action-button')

        # Wait for the game to start and the UI to be responsive
        await page.wait_for_timeout(3000)

        # Define the output path for the screenshot
        screenshot_path = "jules-scratch/verification/verification.png"
        print(f"Taking screenshot: {screenshot_path}")

        # Take a screenshot of the current state of the page
        await page.screenshot(path=screenshot_path)

        await browser.close()
        print("Verification complete. Screenshot saved.")

if __name__ == "__main__":
    asyncio.run(main())
