from playwright.sync_api import Page
import pytest

from pages.bilibili.home_page import HomePage


class TestPlay:
    @pytest.mark.browser_context_args(no_viewport=True, storage_state=".auth/state.json")
    def test_home_page(self, page: Page, pytestconfig, browser_context_args, browser_type_launch_args):
        # Get the response from the HAR file
        # page.set_viewport_size({"width": 1920, "height": 1080})
        print(browser_context_args)
        print(browser_type_launch_args)
        home_page = HomePage(page)
        home_page.navigate()
        links = home_page.links
        home_page.check_links(links)
