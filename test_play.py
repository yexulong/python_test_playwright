from playwright.sync_api import Page
import pytest


class TestPlay:
    @pytest.mark.browser_context_args(no_viewport=True)
    def test_play(self, page: Page, pytestconfig, browser_context_args, browser_type_launch_args):
        # Get the response from the HAR file
        # page.set_viewport_size({"width": 1920, "height": 1080})
        print(browser_context_args)
        print(browser_type_launch_args)
        page.goto("https://www.bilibili.com/")
        heading = page.get_by_role('main').get_by_role('heading')
        print('count:', heading.count())
        links = heading.get_by_role("link")
        for i in range(links.count()):
            print(links.nth(i).inner_text())
