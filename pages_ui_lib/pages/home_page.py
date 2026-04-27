from pages_ui_lib.base_page import BasePage, Button
from pages_ui_lib import locators as loct


class HomePage(BasePage):
    def __init__(self,
                 page,
                 locator=loct.MAIN_PAGE):
        super().__init__(page, locator)

    @property
    def home_button(self):
        return Button(self, loct.GO_HOME_BTN)
