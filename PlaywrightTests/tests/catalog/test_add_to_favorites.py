import pytest
import random
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from data.users import existing_user, new_user
from utils.catalog_helpers import add_n_random_books_to_favorites

def test_register_login_add_books_to_favorites(page, base_url):
    # Limpiar wishlist si hay libros
    page.goto(f"{base_url}/wishlist")
    try:
        clear_btn = page.query_selector('button:has-text("Clear Wishlist")')
        if clear_btn:
            clear_btn.click()
            # Esperar a que la lista se vacíe
            page.wait_for_selector('[data-testid="book-title"]', state='detached', timeout=5000)
    except Exception:
        pass
    """
    1. Registra un usuario nuevo
    2. Hace login
    3. Añade libros random a favoritos
    """
    user = new_user()
    register = RegisterPage(page, base_url)
    register.go()
    register.register(user)
    login = LoginPage(page, base_url)
    login.login(user)
    # Mejor práctica: navegar explícitamente al home tras login
    home = HomePage(page, base_url)
    home.go()
    # Esperar a que los libros sean visibles
    page.wait_for_selector('app-book-card', timeout=5000)
    # Añadir libros y guardar títulos
    titles = []
    cards = page.query_selector_all('app-book-card')
    books = random.sample(cards, min(2, len(cards)))
    for card in books:
        title_el = card.query_selector('[data-testid="book-title"]')
        title = title_el.inner_text().strip() if title_el else None
        fav_btn = card.query_selector('[data-testid="add-to-favorites"]')
        if fav_btn:
            fav_btn.click()
            if title:
                titles.append(title)
    # ...existing code...
    # Navegar a la lista de favoritos
    page.goto(f"{base_url}/wishlist")
    page.wait_for_selector('[data-testid="book-title"]', timeout=5000)
    # Validar que los títulos añadidos están en la lista de favoritos
    wishlist_titles = [el.inner_text().strip() for el in page.query_selector_all('[data-testid="book-title"]')]
    print(f"Libros añadidos a favoritos: {len(titles)}")
    print(f"Libros en la wishlist: {len(wishlist_titles)}")
    for t in titles:
        assert t in wishlist_titles, f"El libro '{t}' no está en la lista de favoritos"

def test_login_existing_user_add_books_to_favorites(page, base_url):
    # Limpiar wishlist si hay libros
    page.goto(f"{base_url}/wishlist")
    try:
        clear_btn = page.query_selector('button:has-text("Clear Wishlist")')
        if clear_btn:
            clear_btn.click()
            # Esperar a que la lista se vacíe
            page.wait_for_selector('[data-testid="book-title"]', state='detached', timeout=5000)
    except Exception:
        pass
    """
    1. Login con usuario existente
    2. Añade libros random a favoritos
    """
    user = existing_user()
    login = LoginPage(page, base_url)
    login.go()
    login.login(user)
    # Mejor práctica: navegar explícitamente al home tras login
    home = HomePage(page, base_url)
    home.go()
    # Esperar a que los libros sean visibles
    page.wait_for_selector('app-book-card', timeout=5000)
    # Añadir libros y guardar títulos
    titles = []
    cards = page.query_selector_all('app-book-card')
    books = random.sample(cards, min(2, len(cards)))
    for card in books:
        title_el = card.query_selector('[data-testid="book-title"]')
        title = title_el.inner_text().strip() if title_el else None
        fav_btn = card.query_selector('[data-testid="add-to-favorites"]')
        if fav_btn:
            fav_btn.click()
            if title:
                titles.append(title)
    # Navegar a la lista de favoritos
    page.goto(f"{base_url}/wishlist")
    page.wait_for_selector('[data-testid="book-title"]', timeout=5000)
    # Validar que los títulos añadidos están en la lista de favoritos
    wishlist_titles = [el.inner_text().strip() for el in page.query_selector_all('[data-testid="book-title"]')]
    print(f"Libros añadidos a favoritos: {len(titles)}")
    print(f"Libros en la wishlist: {len(wishlist_titles)}")
    for t in titles:
        assert t in wishlist_titles, f"El libro '{t}' no está en la lista de favoritos"

