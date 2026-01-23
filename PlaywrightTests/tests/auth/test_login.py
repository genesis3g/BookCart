"""
Tests de login para BookCart
"""
from pages.login_page import LoginPage
from data.users import PLAYWRIGHT_USER, QUEMOLLE_USER, User


# Login con usuario válido playwright
def test_login_with_valid_credentials_playwright(page, base_url):
    """Test: Login exitoso con usuario playwright"""
    login_page = LoginPage(page, base_url)
    
    login_page.open()
    login_page.assert_loaded()
    
    login_page.login(PLAYWRIGHT_USER)
    login_page.assert_logged_in()


# Login con usuario válido quemolle
def test_login_with_valid_credentials_quemolle(page, base_url):
    """Test: Login exitoso con usuario quemolle"""
    login_page = LoginPage(page, base_url)
    
    login_page.open()
    login_page.assert_loaded()
    
    login_page.login(QUEMOLLE_USER)
    login_page.assert_logged_in()


# Login con usuario credenciales inexistentes: debe fallar
def test_login_with_invalid_credentials(page, base_url):
    """Test: Login fallido con credenciales inválidas"""
    invalid_user = User(
        username="invalid_user_xyz",
        password="wrong_password_123"
    )
    
    login_page = LoginPage(page, base_url)
    
    login_page.open()
    login_page.assert_loaded()
    
    login_page.login(invalid_user)
    login_page.assert_login_failed()


# Intenta loguear sin ingresar username: debe fallar
def test_login_empty_username(page, base_url):
    """Test: Intenta loguear sin username (debería fallar)"""
    invalid_user = User(username="", password="password123")
    
    login_page = LoginPage(page, base_url)
    login_page.open()
    login_page.assert_loaded()
    
    # Intenta enviar sin username
    login_page._password_input().fill(invalid_user.password)
    login_page._login_button().click()
    
    # Falla y sigue en la página de login
    assert page.url == f"{base_url}/login"


# Intenta loguear sin ingresar password: debe fallar
def test_login_empty_password(page, base_url):
    """Test: Intenta loguear sin password (debería fallar)"""
    login_page = LoginPage(page, base_url)
    
    login_page.open()
    login_page.assert_loaded()
    
    # Enviar sin password
    login_page._username_input().fill("playwright")
    login_page._login_button().click()
    
    # Falla y sigue en la página de login
    assert page.url == f"{base_url}/login"
