# Helpers para catálogo y acciones sobre libros
import random
from playwright.sync_api import Page


def get_visible_book_cards(page: Page):
    """Devuelve una lista de elementos de libro visibles en el home."""
    return page.query_selector_all('app-book-card')


def pick_random_book_card(page: Page):
    """Selecciona un libro random de los visibles."""
    cards = get_visible_book_cards(page)
    if not cards:
        raise Exception('No hay libros visibles en el catálogo.')
    return random.choice(cards)


def add_random_book_to_cart(page: Page):
    """Añade un libro random al carrito desde el home."""
    card = pick_random_book_card(page)
    add_btn = card.query_selector('[data-testid="add-to-cart"]')
    if add_btn:
        add_btn.click()
        return True
    return False


def add_random_book_to_favorites(page: Page):
    """Añade un libro random a favoritos desde el home (si el botón está presente)."""
    card = pick_random_book_card(page)
    fav_btn = card.query_selector('[data-testid="add-to-favorites"]')
    if fav_btn:
        fav_btn.click()
        return True
    return False


def add_n_random_books_to_cart(page: Page, n=1):
    """Añade n libros random al carrito."""
    cards = get_visible_book_cards(page)
    if not cards:
        raise Exception('No hay libros visibles en el catálogo.')
    books = random.sample(cards, min(n, len(cards)))
    for card in books:
        add_btn = card.query_selector('[data-testid="add-to-cart"]')
        if add_btn:
            add_btn.click()


def add_n_random_books_to_favorites(page: Page, n=1):
    """Añade n libros random a favoritos (si el botón está presente)."""
    cards = get_visible_book_cards(page)
    if not cards:
        raise Exception('No hay libros visibles en el catálogo.')
    books = random.sample(cards, min(n, len(cards)))
    for card in books:
        # Mejor práctica: buscar data-testid o atributos únicos
        title = None
        selector_usado = None
        # 1. data-testid
        title_el = card.query_selector('[data-testid="book-title"]')
        if title_el:
            title = title_el.inner_text().strip()
            selector_usado = '[data-testid="book-title"]'
        else:
            # 2. mat-card-title
            title_el = card.query_selector('mat-card-title')
            if title_el:
                title = title_el.inner_text().strip()
                selector_usado = 'mat-card-title'
            else:
                # 3. h2
                h2 = card.query_selector('h2')
                if h2:
                    title = h2.inner_text().strip()
                    selector_usado = 'h2'
        fav_btn = card.query_selector('[data-testid="add-to-favorites"]')
        if fav_btn:
            fav_btn.click()
            print(f"Añadido a favoritos: {title if title else '[sin título encontrado]'} (selector: {selector_usado if selector_usado else 'ninguno'})")
        else:
            print(f"No se encontró botón de favorito para: {title if title else '[sin título encontrado]'} (selector: {selector_usado if selector_usado else 'ninguno'})")
        if not title:
            print("SUGERENCIA: Agrega data-testid=\"book-title\" al elemento del título del libro para facilitar la automatización.")
