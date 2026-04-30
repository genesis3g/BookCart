from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def navigate(self, path: str = "") -> None:
        self.page.goto(path)

    def wait_for_url(self, pattern: str) -> None:
        self.page.wait_for_url(pattern)

    def get_title(self) -> str:
        return self.page.title()
