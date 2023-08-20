from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)
        self.links = page.get_by_role('main').get_by_role('heading').get_by_role("link")

    def navigate(self):
        self.page.goto('/')
