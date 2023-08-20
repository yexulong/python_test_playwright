import os
from typing import Generator, Callable, Dict, List, Any

import pytest
import allure
from playwright.sync_api import Browser, Error, Page, BrowserContext
from pytest_playwright.pytest_playwright import artifacts_folder, _build_artifact_test_folder
from slugify import slugify


# @pytest.fixture(scope="session")
# def browser(launch_browser: Callable[[], Browser], pytestconfig: Any) -> Generator[Browser, None, None]:
#     launch_args = []
#     maximized_option = pytestconfig.getoption('--start-maximized')
#     if maximized_option:
#         launch_args.append('--start-maximized')
#     print(launch_args)
#     browser = launch_browser(args=launch_args)
#     yield browser
#     browser.close()
#     artifacts_folder.cleanup()

# @pytest.fixture(scope="session")
# def browser_context_args(
#     browser_context_args,
#     pytestconfig: Any
# ) -> Dict:
#     context_option = {}
#     # viewport_option = pytestconfig.getoption('--viewport')
#     # if viewport_option:
#     #     context_option['viewport'] = viewport_option
#     # else:
#     context_option['no_viewport'] = True
#     return {
#         **browser_context_args,
#         **context_option
#     }