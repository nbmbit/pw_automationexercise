from playwright.sync_api import Playwright, expect

from pages.home_page import HomePage


def test_home_page_visible(launch_browser):
    page = launch_browser
    home_page = HomePage(page)

    home_page.close_all_popups()

    expect(home_page.unique_element).to_be_visible()


def test_home_page_login(launch_browser):
    pass
