"""
Clase base para Page Objects
"""
from playwright.sync_api import Page


class BasePage:
    """Clase base para todos los Page Objects"""
    
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
    
    def goto(self, path: str):
        """Navega a una URL relativa"""
        full_url = f"{self.base_url}{path}"
        self.page.goto(full_url)
        return self
    
    def wait_for_load(self, timeout: int = 5000):
        """Espera a que la página cargue"""
        self.page.wait_for_load_state("networkidle", timeout=timeout)
        return self
