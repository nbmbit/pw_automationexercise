from pages.base_page import PopupPage
from pages import locators as loct
from pages.locales import locales as locl


class SelectLocationPopup(PopupPage):
    def __init__(self,
                 page,
                 main_text=locl['popups']['location']['main'],
                 popup_locator=loct.GEOIP_POPUP
                 ):
        super().__init__(
            page=page,
            popup_locator=popup_locator,
            main_text=main_text
            )
        self.yes_button = page.get_by_role("button", name='Yes')
        self.no_button = page.get_by_role("button", name='No')
        self.close_button = page.locator(loct.GEOIP_CLOSE_BTN)
