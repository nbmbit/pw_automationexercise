import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def launch_browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.jonessnowboards.com/")

        yield page

        browser.close()
