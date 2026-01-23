# playwright_tests/pages/login_page.py
import re
from playwright.sync_api import expect, Page
from .base_page import BasePage
from data.users import User

class LoginPage(BasePage):
    PATH = "/login"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)

    # --- Selectores directos basados en tu HTML ---
    def _username_input(self):
        return self.page.locator('input[formcontrolname="username"], input[formcontrolname*="user" i]').first

    def _password_input(self):
        return self.page.locator('input[formcontrolname="password"], input[type="password"]').first

    def _login_button(self):
        # Buscar el botón dentro del mat-card (no el del header)
        card = self.page.locator("mat-card")
        if card.count() > 0:
            # Buscar solo dentro del card
            btn = card.first.locator("button:has-text('Login')")
            if btn.count() > 0:
                return btn.first
        # Fallback: usar role button
        return self.page.get_by_role("button", name=re.compile(r"^login$", re.I)).last

    # --- Acciones / Asserts ---
    def open(self):
        self.goto(self.PATH)
        self.assert_loaded()
        return self

    def assert_loaded(self):
        # Verifica que el título del card "Login" esté presente
        title = self.page.get_by_text(re.compile(r"^\s*Login\s*$", re.I))
        expect(title.first).to_be_visible()
        # y que exista al menos el password input
        expect(self._password_input()).to_be_visible()
        return self

    def login(self, user: User):
        # rellenar y enviar
        self._username_input().fill(user.username)
        self._password_input().fill(user.password)
        self._login_button().click()
        return self

    def assert_login_failed(self):
        # Material muestra errores en mat-error o snack-bar. Detecta ambos.
        err = self.page.locator("mat-error, .mat-mdc-snack-bar-container, .mat-mdc-simple-snack-bar")
        expect(err.first).to_be_visible()
        return self

    def assert_logged_in(self):
        # Después de login exitoso, debería estar en / (home)
        expect(self.page).not_to_have_url(re.compile(r"/login", re.I))
        return self
