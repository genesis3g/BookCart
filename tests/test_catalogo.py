from playwright.sync_api import Page, expect
import os

BASE_URL = os.getenv("BASE_URL", "http://localhost:4200")

def test_filter_by_category_shows_fiction(page: Page):
    page.goto(BASE_URL, wait_until="networkidle")

    page.get_by_text("Fiction", exact=True).first.click()

    expect(page.get_by_role("link", name="Dune")).to_be_visible()

    cards = page.locator("app-book-card")
    expect(cards.first).to_be_visible()
