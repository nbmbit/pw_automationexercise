import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def set_up_sess():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://automationexercise.com/")

        yield page

        browser.close()


@pytest.fixture
def set_up(page):
    page.goto("https://automationexercise.com/")
    page.wait_for_load_state("networkidle")

    yield page

    page.close()
