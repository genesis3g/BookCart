# playwright_tests/tests/auth/test_register_and_login.py
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from data.users import new_user

def test_register_then_login(page, base_url):
    user = new_user()

    # 1) Abrir home y navegar a login
    login_page = LoginPage(page, base_url)
    login_page.open()
    login_page.assert_loaded()

    # 2) Desde login, navegar a registro
    login_page.go_to_register()

    # 3) Registrar
    register = RegisterPage(page, base_url)
    register.assert_loaded()
    register.register(user)
    register.assert_registration_success()

    # 4) Volver a login y loguear
    login_page.open()
    login_page.assert_loaded()
    login_page.login(user)

    # 5) Verificar login exitoso
    login_page.assert_logged_in()
