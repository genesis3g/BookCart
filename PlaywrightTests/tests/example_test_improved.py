"""
Ejemplo de test mejorado usando Page Objects y Flows
Este archivo demuestra las mejores prácticas implementadas
"""
import pytest
from flows.auth_flow import AuthFlow
from flows.catalog_flow import CatalogFlow
from flows.order_flow import OrderFlow
from data.test_data_builder import TestDataBuilder


class TestAuthenticationExample:
    """Suite de tests de autenticación usando el patrón mejorado"""
    
    def test_login_successful(self, auth_flow):
        """Test: Login exitoso con usuario válido"""
        # Usar el flow en lugar de interactuar directamente con la página
        auth_flow.login_as_customer()
        
        # El flow maneja las validaciones internamente
    
    def test_login_with_invalid_credentials(self, auth_flow):
        """Test: Login fallido con credenciales inválidas"""
        auth_flow.try_invalid_login()
    
    def test_register_new_user(self, auth_flow):
        """Test: Registro de nuevo usuario"""
        auth_flow.register_new_user()


class TestCatalogExample:
    """Suite de tests de catálogo usando el patrón mejorado"""
    
    def test_add_book_to_cart(self, catalog_flow):
        """Test: Agregar un libro al carrito"""
        catalog_flow.open_catalog()
        catalog_flow.add_random_book_to_cart()
    
    def test_add_multiple_books_to_cart(self, catalog_flow):
        """Test: Agregar múltiples libros al carrito"""
        catalog_flow.open_catalog()
        catalog_flow.add_multiple_books_to_cart(5)
    
    def test_add_book_to_favorites(self, catalog_flow):
        """Test: Agregar un libro a favoritos"""
        catalog_flow.open_catalog()
        catalog_flow.add_book_to_favorites()


class TestOrderExample:
    """Suite de tests de órdenes usando el patrón mejorado"""
    
    def test_complete_purchase(self, user_with_items_in_cart, order_flow):
        """Test: Completar un pedido"""
        order_flow.complete_purchase(
            address="123 Test Street",
            city="Test City",
            zip_code="12345"
        )


class TestE2EExample:
    """Suite de tests E2E (End-to-End)"""
    
    def test_full_user_journey(self, page, base_url, auth_flow, catalog_flow, order_flow):
        """Test: Flujo completo de usuario (login -> shopping -> checkout)"""
        # 1. Login
        auth_flow.login_as_customer()
        
        # 2. Navegar catálogo y agregar items
        catalog_flow.open_catalog()
        catalog_flow.add_multiple_books_to_cart(3)
        catalog_flow.add_book_to_favorites()
        
        # 3. Realizar compra
        order_flow.go_to_cart()
        order_flow.proceed_to_checkout()
        order_flow.fill_shipping_info(
            address="456 Main St",
            city="Anytown",
            zip_code="54321"
        )
        order_flow.fill_payment_info()
        order_flow.place_order()
        order_flow.verify_order_confirmation()
