from playwright.sync_api import Page, expect
import os

BASE_URL = os.getenv("BASE_URL", "http://localhost:4200")

def test_home_loads_and_shows_books(page: Page):
    page.goto(BASE_URL, wait_until="networkidle")

    expect(page.get_by_role("link", name="Clean Code")).to_be_visible()
    expect(page.get_by_role("link", name="Dune")).to_be_visible()
