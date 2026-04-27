from playwright.sync_api import expect
import pytest

from pages_ui_lib.pages.home_page import HomePage


@pytest.mark.smoke
def test_home_page_visible(set_up):
    home_page = HomePage(set_up)

    home_page.close_all_popups()

    expect(home_page.unique_element).to_be_visible()


def test_home_page_login(set_up):
    pass


def test_home_page_logout(set_up):
    pass
