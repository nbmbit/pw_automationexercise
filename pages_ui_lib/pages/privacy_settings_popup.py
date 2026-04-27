from pages_ui_lib.base_page import BasePage
from pages_ui_lib import locators as loct


class PrivacySettingsPopup(BasePage):
    def __init__(self,
                 page,
                 locator=loct.PRIVACY_POPUP
                 ):
        super().__init__(
            page=page,
            locator=locator
        )

    @property
    def consent_button(self):
        return self.page.get_by_role("button", name="Consent")

    @property
    def manage_button(self):
        return self.page.get_by_role("button", name="Manage options")
