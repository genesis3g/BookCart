"""
Componente de header reutilizable
"""
from pages.base_page import BasePage


class HeaderComponent(BasePage):
    """Componente de header compartido entre páginas"""
    
    # Selectores
    LOGO = "app-header [data-testid='logo']"
    HOME_LINK = "app-header [data-testid='home-link']"
    CART_LINK = "app-header [data-testid='cart-link']"
    WISHLIST_LINK = "app-header [data-testid='wishlist-link']"
    LOGIN_LINK = "app-header [data-testid='login-link']"
    REGISTER_LINK = "app-header [data-testid='register-link']"
    USER_MENU = "app-header [data-testid='user-menu']"
    LOGOUT_BUTTON = "app-header [data-testid='logout-button']"
    SEARCH_INPUT = "app-header [data-testid='search-input']"
    SEARCH_BUTTON = "app-header [data-testid='search-button']"
    
    def go_to_home(self):
        """Navega a home"""
        self.click(self.HOME_LINK)
        return self
    
    def go_to_cart(self):
        """Navega al carrito"""
        self.click(self.CART_LINK)
        return self
    
    def go_to_wishlist(self):
        """Navega a favoritos"""
        self.click(self.WISHLIST_LINK)
        return self
    
    def go_to_login(self):
        """Navega a login"""
        self.click(self.LOGIN_LINK)
        return self
    
    def go_to_register(self):
        """Navega a registro"""
        self.click(self.REGISTER_LINK)
        return self
    
    def search(self, query: str):
        """Realiza una búsqueda"""
        self.fill(self.SEARCH_INPUT, query)
        self.click(self.SEARCH_BUTTON)
        return self
    
    def open_user_menu(self):
        """Abre el menú de usuario"""
        self.click(self.USER_MENU)
        return self
    
    def logout(self):
        """Realiza logout"""
        self.open_user_menu()
        self.click(self.LOGOUT_BUTTON)
        return self
    
    def is_logged_in(self) -> bool:
        """Verifica si hay un usuario logueado"""
        return self.element_is_visible(self.USER_MENU)
