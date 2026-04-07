from pages.base_page import BasePage
from pages import locators as loct


class HomePage(BasePage):
    def __init__(self,
                 page,
                 popup_locator=loct.MAIN_PAGE):
        super().__init__(page, popup_locator)

    def go_home_page(self):
        self.page.locator(loct.GO_HOME_BTN).click()

    def close_all_popups(self):
        for btn in ['No', 'Accept']:
            btn = self.page.get_by_role("button", name=btn)
            if btn.is_visible():
                btn.click()
                self.page.wait_for_load_state('networkidle')
