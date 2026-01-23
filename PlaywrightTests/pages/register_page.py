"""
Page Object para el formulario de registro de usuarios
"""
from playwright.sync_api import Page, expect
import re
from data.users import User


class RegisterPage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.url = f"{base_url}/register"

    # Selectores
    @property
    def first_name_input(self):
        return self.page.locator('input[formcontrolname="firstName"]')

    @property
    def last_name_input(self):
        return self.page.locator('input[formcontrolname="lastName"]')

    @property
    def username_input(self):
        return self.page.locator('input[formcontrolname="userName"]')

    @property
    def password_input(self):
        return self.page.locator('input[formcontrolname="password"]')

    @property
    def confirm_password_input(self):
        return self.page.locator('input[formcontrolname="confirmPassword"]')

    @property
    def gender_select(self):
        # Selecciona los input radio dentro de mat-radio-button
        return self.page.locator('mat-radio-button input[type="radio"]')

    @property
    def register_button(self):
        # Buscar el botón Register dentro del mat-card
        card = self.page.locator("mat-card")
        if card.count() > 0:
            btn = card.first.locator("button:has-text('Register')")
            if btn.count() > 0:
                return btn.first
        return self.page.get_by_role("button", name=re.compile(r"^register$", re.I)).last

    @property
    def page_title(self):
        return self.page.get_by_text(re.compile(r"^\s*User Registration\s*$", re.IGNORECASE))

    @property
    def error_messages(self):
        return self.page.locator("mat-error")

    # Acciones
    def open(self):
        """Abre la página de registro"""
        self.page.goto(self.url)
        return self

    def assert_loaded(self):
        """Verifica que la página de registro esté cargada"""
        expect(self.page_title).to_be_visible()
        expect(self.first_name_input).to_be_visible()
        expect(self.last_name_input).to_be_visible()
        expect(self.username_input).to_be_visible()
        expect(self.password_input).to_be_visible()
        expect(self.confirm_password_input).to_be_visible()
        return self

    def register(self, user: User, first_name: str = "Test", last_name: str = "User", gender: str = "Male"):
        """Completa el formulario de registro con los datos del usuario"""
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.username_input.fill(user.username)
        self.password_input.fill(user.password)
        self.confirm_password_input.fill(user.password)

        # Seleccionar género (input radio)
        gender_buttons = self.gender_select
        found = False
        for i in range(gender_buttons.count()):
            btn = gender_buttons.nth(i)
            # Buscar el label asociado para comparar texto
            label = btn.evaluate("el => el.closest('mat-radio-button').textContent")
            if label and gender.lower() in label.lower():
                btn.click()
                found = True
                # Validar que quedó seleccionado
                if not btn.is_checked():
                    raise AssertionError(f"No se pudo seleccionar el género '{gender}'")
                break
        if not found:
            raise AssertionError(f"No se encontró el género '{gender}' en el formulario")

        # Intentar submit: primero con click al botón
        self.register_button.click()

        # Si no funciona el click, intentar con Enter
        import time
        time.sleep(1)
        if self.page.url == f"{self.base_url}/register":
            # El click no funcionó, intentar con Enter
            self.confirm_password_input.press("Enter")

        return self

    def assert_registration_success(self):
        """Verifica que el registro fue exitoso (debería redirigir a login o home)"""
        expect(self.page).not_to_have_url(re.compile(r"/register", re.I))
        return self

    def assert_registration_failed(self):
        """Verifica que el registro falló (errores visibles)"""
        expect(self.error_messages.first).to_be_visible()
        return self

    def get_error_text(self) -> str:
        """Obtiene el texto del primer error"""
        if self.error_messages.count() > 0:
            return self.error_messages.first.text_content()
        return ""
