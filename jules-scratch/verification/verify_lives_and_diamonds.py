import os
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Construct the file path to index.html
        file_path = "file://" + os.path.abspath("index.html")
        page.goto(file_path)

        # Start the game
        page.click("#action-button")

        # Wait for the UI to be in the correct state
        page.wait_for_selector("#livesDisplay", state="visible")
        page.wait_for_selector("#diamondsDisplay", state="visible")

        # Take a screenshot
        page.screenshot(path="jules-scratch/verification/verification.png")

        browser.close()

if __name__ == "__main__":
    run()
