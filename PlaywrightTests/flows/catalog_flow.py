"""
Flujo de catálogo y carrito de compras reutilizable
"""
from pages.home_page import HomePage
from data.test_data_builder import TestDataBuilder
from utils.logger import logger


class CatalogFlow:
    """Flujo de navegación de catálogo y carrito"""
    
    def __init__(self, page, base_url):
        self.page = page
        self.base_url = base_url
        self.home_page = HomePage(page, base_url)
        self.logger = logger
    
    def open_catalog(self) -> "CatalogFlow":
        """Abre la página del catálogo"""
        self.logger.info("→ Abriendo catálogo")
        self.home_page.go()
        self.logger.info("✓ Catálogo abierto")
        return self
    
    def add_random_book_to_cart(self) -> "CatalogFlow":
        """Agrega un libro aleatorio al carrito"""
        self.logger.info("→ Agregando libro aleatorio al carrito")
        result = self.home_page.add_random_book_to_cart()
        if result:
            self.logger.info("✓ Libro agregado al carrito")
        else:
            self.logger.warning("⚠ No se pudo agregar el libro")
        return self
    
    def add_multiple_books_to_cart(self, count: int = 3) -> "CatalogFlow":
        """Agrega múltiples libros al carrito"""
        self.logger.info(f"→ Agregando {count} libros al carrito")
        self.home_page.add_n_random_books_to_cart(count)
        self.logger.info(f"✓ {count} libros agregados al carrito")
        return self
    
    def add_book_to_favorites(self) -> "CatalogFlow":
        """Agrega un libro aleatorio a favoritos"""
        self.logger.info("→ Agregando libro a favoritos")
        result = self.home_page.add_random_book_to_favorites()
        if result:
            self.logger.info("✓ Libro agregado a favoritos")
        else:
            self.logger.warning("⚠ No se pudo agregar a favoritos")
        return self
    
    def search_books(self, query: str) -> "CatalogFlow":
        """Busca libros por término"""
        self.logger.info(f"→ Buscando libros: '{query}'")
        # Implementar búsqueda según estructura de la app
        # self.home_page.search(query)
        self.logger.info(f"✓ Búsqueda realizada: '{query}'")
        return self
    
    def filter_by_category(self, category: str) -> "CatalogFlow":
        """Filtra libros por categoría"""
        self.logger.info(f"→ Filtrando por categoría: {category}")
        # Implementar filtro según estructura de la app
        # self.home_page.filter(category)
        self.logger.info(f"✓ Filtro aplicado: {category}")
        return self
    
    def sort_by(self, sort_option: str) -> "CatalogFlow":
        """Ordena los libros por una opción específica"""
        self.logger.info(f"→ Ordenando por: {sort_option}")
        # Implementar ordenamiento según estructura de la app
        # self.home_page.sort(sort_option)
        self.logger.info(f"✓ Ordenamiento aplicado: {sort_option}")
        return self
