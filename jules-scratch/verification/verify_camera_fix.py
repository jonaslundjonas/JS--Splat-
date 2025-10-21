from playwright.sync_api import sync_playwright
import os

def run_verification():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        file_path = os.path.abspath('index.html')
        page.goto(f'file://{file_path}')

        # Click the body to focus and then the start button
        page.locator('body').click()
        page.wait_for_timeout(200)
        page.locator('#action-button').click()

        # Wait for the game to enter the running state.
        page.wait_for_timeout(1000)

        # Simulate turning left
        page.keyboard.down('KeyQ')
        page.wait_for_timeout(500)
        page.keyboard.up('KeyQ')

        page.wait_for_timeout(200)

        # Simulate turning right
        page.keyboard.down('KeyE')
        page.wait_for_timeout(500)
        page.keyboard.up('KeyE')

        page.wait_for_timeout(200)

        # Take a screenshot
        page.screenshot(path='jules-scratch/verification/verification.png')

        browser.close()

if __name__ == '__main__':
    run_verification()
