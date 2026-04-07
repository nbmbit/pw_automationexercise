

class BasePage:
    def __init__(self, page, popup_locator):
        self.page = page
        self.popup_locator = page.locator(popup_locator)
        self.unique_element = self.popup_locator

    def is_visible(self):
        return self.unique_element.is_visible()

    def is_hidden(self):
        return self.unique_element.is_hidden()


class PopupPage:
    def __init__(self, page, popup_locator, title=None, main_text=None):
        self.popup_locator = page.locator(popup_locator)
        self.title = None if not title else page.get_by_text(title)
        self.main_text = None if not main_text else page.get_by_text(main_text)
        self.unique_element = self.popup_locator

    def is_visible(self):
        return self.unique_element.is_visible()

    def is_hidden(self):
        return self.unique_element.is_hidden()
