import allure
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def navigate(self):
        pass

    def check_links(self, locator):
        print('count:', locator.count())
        for i in range(locator.count()):
            link = locator.nth(i)
            title = link.inner_text()
            with allure.step(f'检查链接: {title}'):
                with self.page.expect_popup() as page2_info:
                    link.click()
                page2 = page2_info.value
                expect(page2.get_by_role('heading').first).to_have_text(title)
                page2.close()
