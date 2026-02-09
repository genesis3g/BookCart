import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from data.users import existing_user, new_user
from utils.catalog_helpers import add_n_random_books_to_cart, add_n_random_books_to_favorites


def test_register_login_add_books_to_cart(page, base_url):
    """
    1. Registra un usuario nuevo
    2. Hace login
    3. Añade libros random al carrito
    """
    user = new_user()
    register = RegisterPage(page, base_url)
    register.go()
    register.register(user)
    login = LoginPage(page, base_url)
    login.login(user)
    home = HomePage(page, base_url)
    home.go()
    add_n_random_books_to_cart(page, n=2)
    # Validar que el carrito tiene libros (puedes expandir asserts según UI)
    # ...

def test_login_existing_user_add_books_to_cart(page, base_url):
    """
    1. Login con usuario existente
    2. Añade libros random al carrito
    3. Revisa el carrito
    """
    user = existing_user()
    login = LoginPage(page, base_url)
    login.go()
    login.login(user)
    home = HomePage(page, base_url)
    home.go()
    add_n_random_books_to_cart(page, n=2)
    # Validar que el carrito tiene libros (puedes expandir asserts según UI)
    # ...
