from playwright.sync_api import sync_playwright
import os

def verify_graphics():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Get the absolute path to index.html
        html_file_path = os.path.abspath('index.html')

        # Navigate to the local file
        page.goto(f'file://{html_file_path}')

        # Wait for the DOM to be loaded
        page.wait_for_load_state('domcontentloaded')

        # Take a screenshot
        page.screenshot(path='jules-scratch/verification/verification.png')

        browser.close()

if __name__ == '__main__':
    verify_graphics()
