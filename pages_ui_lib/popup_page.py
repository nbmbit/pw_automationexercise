

from pages_ui_lib.base_page import BasePage


class PopupPage(BasePage):
    def __init__(self,
                 page,
                 popup_locator):
        super().__init__(page,
                         popup_locator)
