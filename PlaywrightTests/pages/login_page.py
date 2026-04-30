from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self._username = page.get_by_placeholder("Username")
        self._password = page.get_by_placeholder("Password")
        self._login_btn = page.get_by_role("button", name="Login", exact=True)
        self._register_btn = page.get_by_role("button", name="Register")
        self._error = page.locator("mat-error", has_text="Login Failed")

    def navigate(self) -> None:
        super().navigate("/login")

    def login(self, username: str, password: str) -> None:
        self.navigate()
        self._username.fill(username)
        self._password.fill(password)
        self._login_btn.click()

    def go_to_register(self) -> None:
        self._register_btn.click()

    def is_error_visible(self) -> bool:
        return self._error.is_visible()
