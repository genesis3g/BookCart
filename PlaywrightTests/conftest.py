import pytest
from utils.api_client import ApiClient

BASE_URL = "https://localhost:7073"


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args: dict) -> dict:
    return {**browser_context_args, "ignore_https_errors": True}


@pytest.fixture(scope="session")
def api() -> ApiClient:
    return ApiClient(BASE_URL)


@pytest.fixture
def logged_in_page(page, api):
    """Page with an authenticated session using the fixed playwright user."""
    from pages.login_page import LoginPage
    from data.users import PLAYWRIGHT_USER

    LoginPage(page).login(PLAYWRIGHT_USER["username"], PLAYWRIGHT_USER["password"])
    return page
