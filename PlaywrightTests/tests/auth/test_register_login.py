# playwright_tests/tests/auth/test_register_and_login.py
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from data.users import new_user

def test_register_then_login(page, base_url):
    user = new_user()

    # 1) Abrir home y navegar a register
    home = HomePage(page, base_url).open()
    home.header().go_to_register()

    # 2) Registrar
    register = RegisterPage(page, base_url)
    register.assert_loaded()
    register.register(user)
    register.assert_success()  # según impl. del RegisterPage puede validar toast o redirección

    # 3) Ir a login (header tiene botón Register; asumimos similar para login)
    home.header().go_to_login()

    # 4) Login
    login = LoginPage(page, base_url)
    login.assert_loaded()
    login.login(user)

    # 5) Verificar login exitoso
    login.assert_logged_in()
