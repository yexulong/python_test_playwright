from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.bilibili.com/")
    page.pause()
    # ---------------------在暂停之后登录
    storage = context.storage_state(path="state.json")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
