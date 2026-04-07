from pages.base_page import PopupPage
from pages import locators as loct
from pages.locales import locales as locl


class PrivacySettingsPopup(PopupPage):
    def __init__(self,
                 page,
                 title=locl['popups']['privacy']['title'],
                 main_text=locl['popups']['privacy']['main'],
                 popup_locator=loct.PRIVACY_POPUP
                 ):
        super().__init__(
            page=page,
            popup_locator=popup_locator,
            title=title,
            main_text=main_text
        )
        self.accept_button = page.get_by_role("button", name='Accept')
        self.decline_button = page.get_by_role("button", name='Decline')
        self.manage_button = page.get_by_role("button", name='Manage')
