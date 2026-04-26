from playwright.sync_api import expect


class BasePage:
    def __init__(self, page, locator):
        self.page = page
        if isinstance(locator, tuple):
            self.locator = \
                self.page.get_by_role(locator[0], name=locator[1])
        else:
            self.locator = self.page.locator(locator)
        self.unique_element = self.locator

    def __getattr__(self, name):
        return getattr(self.page, name)

    @property
    def expect(self):
        return expect(self.locator)

    def is_visible(self):
        return self.locator.is_visible()

    def is_hidden(self):
        return self.locator.is_hidden()

    def close_all_popups(self):
        for btn in ['Consent', ]:
            btn = self.page.get_by_role("button", name=btn)
            if btn.is_visible():
                btn.click()
                self.page.wait_for_load_state('networkidle')


class Button():
    def __init__(self, page, locator):
        self.page = page
        self.locator = self.page.get_by_role(locator[0], name=locator[1])

    def click(self):
        self.locator.click()

    def is_selected(self):
        style = self.locator.get_attribute("style") or ""
        return "orange" in style
