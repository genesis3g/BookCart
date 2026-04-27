"""
Page Object para la página de inicio
"""
from playwright.sync_api import Page
from pages.base_page import BasePage
from pages.common_page import HeaderComponent
from utils.logger import logger


class HomePage(BasePage):
    """Page Object para la página de inicio"""
    
    # Selectores
    BOOK_CARDS = "app-book-card"
    ADD_TO_CART_BTN = "[data-testid='add-to-cart']"
    ADD_TO_FAVORITES_BTN = "[data-testid='add-to-favorites']"
    BOOK_TITLE = "[data-testid='book-title']"
    BOOK_PRICE = "[data-testid='book-price']"
    CATALOG_CONTAINER = "app-catalog"
    FEATURED_BOOKS = "[data-testid='featured-books']"
    CATEGORIES_FILTER = "[data-testid='categories']"
    SEARCH_INPUT = "[data-testid='search-catalog']"
    SORT_DROPDOWN = "[data-testid='sort-by']"
    
    def __init__(self, page: Page, base_url: str = None):
        super().__init__(page, base_url)
        self.header = HeaderComponent(page, base_url)
    
    def go(self):
        """Navega a la página de inicio"""
        self.goto("")
        self.wait_for_load()
        self.logger.info("HomePage cargada")
        return self
    
    def wait_for_catalog_load(self):
        """Espera a que el catálogo cargue completamente"""
        self.wait_for_element(self.CATALOG_CONTAINER)
        self.logger.debug("Catálogo cargado")
        return self
    
    def get_visible_book_cards(self):
        """Obtiene todos los libros visibles"""
        return self.get_elements(self.BOOK_CARDS)
    
    def get_book_count(self) -> int:
        """Obtiene el número de libros visibles"""
        cards = self.get_visible_book_cards()
        return len(cards)
    
    def pick_book_at_index(self, index: int = 0):
        """Selecciona un libro por índice"""
        cards = self.get_visible_book_cards()
        if index >= len(cards):
            raise IndexError(f"No hay libro en índice {index}. Total: {len(cards)}")
        self.logger.debug(f"Seleccionando libro en índice {index}")
        return cards[index]
    
    def pick_first_book(self):
        """Selecciona el primer libro"""
        return self.pick_book_at_index(0)
    
    def add_random_book_to_cart(self) -> bool:
        """Agrega un libro aleatorio al carrito"""
        import random
        cards = self.get_visible_book_cards()
        if not cards:
            self.logger.error("No hay libros disponibles")
            return False
        
        card = random.choice(cards)
        add_btn = card.query_selector(self.ADD_TO_CART_BTN)
        if add_btn and add_btn.is_visible():
            add_btn.click()
            self.logger.info("Libro agregado al carrito")
            return True
        
        self.logger.warning("Botón 'Agregar al carrito' no disponible")
        return False
    
    def add_random_book_to_favorites(self) -> bool:
        """Agrega un libro aleatorio a favoritos"""
        import random
        cards = self.get_visible_book_cards()
        if not cards:
            self.logger.error("No hay libros disponibles")
            return False
        
        card = random.choice(cards)
        fav_btn = card.query_selector(self.ADD_TO_FAVORITES_BTN)
        if fav_btn and fav_btn.is_visible():
            fav_btn.click()
            self.logger.info("Libro agregado a favoritos")
            return True
        
        self.logger.warning("Botón 'Agregar a favoritos' no disponible")
        return False
    
    def add_n_random_books_to_cart(self, n: int = 1) -> int:
        """Agrega n libros aleatorios al carrito"""
        import random
        cards = self.get_visible_book_cards()
        if not cards:
            self.logger.error("No hay libros disponibles")
            return 0
        
        sample_size = min(n, len(cards))
        books_to_add = random.sample(cards, sample_size)
        
        added_count = 0
        for card in books_to_add:
            add_btn = card.query_selector(self.ADD_TO_CART_BTN)
            if add_btn and add_btn.is_visible():
                add_btn.click()
                added_count += 1
                self.logger.debug(f"Libro agregado ({added_count}/{sample_size})")
        
        self.logger.info(f"Se agregaron {added_count} libros al carrito")
        return added_count
    
    def add_book_to_cart_at_index(self, index: int = 0) -> bool:
        """Agrega un libro específico al carrito por índice"""
        card = self.pick_book_at_index(index)
        add_btn = card.query_selector(self.ADD_TO_CART_BTN)
        if add_btn and add_btn.is_visible():
            add_btn.click()
            self.logger.info(f"Libro en índice {index} agregado al carrito")
            return True
        return False
    
    def search_books(self, query: str):
        """Busca libros por términos"""
        self.fill(self.SEARCH_INPUT, query)
        self.press_key(self.SEARCH_INPUT, "Enter")
        self.logger.info(f"Búsqueda realizada: '{query}'")
        return self
    
    def filter_by_category(self, category: str):
        """Filtra libros por categoría"""
        # Implementar según estructura HTML
        self.logger.info(f"Filtrando por categoría: {category}")
        return self
    
    def sort_by(self, sort_option: str):
        """Ordena los libros"""
        self.select_option(self.SORT_DROPDOWN, sort_option)
        self.logger.info(f"Libros ordenados por: {sort_option}")
        return self
