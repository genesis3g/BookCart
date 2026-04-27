"""
Configuración específica para tests
Aquí puedes agregar fixtures personalizadas por suite de tests
"""
import pytest
from flows.auth_flow import AuthFlow
from flows.catalog_flow import CatalogFlow
from flows.order_flow import OrderFlow


@pytest.fixture
def auth_flow(page, base_url):
    """Fixture para flujo de autenticación"""
    return AuthFlow(page, base_url)


@pytest.fixture
def catalog_flow(page, base_url):
    """Fixture para flujo de catálogo"""
    return CatalogFlow(page, base_url)


@pytest.fixture
def order_flow(page, base_url):
    """Fixture para flujo de órdenes"""
    return OrderFlow(page, base_url)


@pytest.fixture
def logged_in_user(page, base_url):
    """Fixture que crea una sesión de usuario logueado"""
    auth_flow = AuthFlow(page, base_url)
    auth_flow.login_as_customer()
    yield page
    # Cleanup (logout) si es necesario


@pytest.fixture
def user_with_items_in_cart(page, base_url):
    """Fixture que crea un usuario con items en el carrito"""
    auth_flow = AuthFlow(page, base_url)
    catalog_flow = CatalogFlow(page, base_url)
    
    auth_flow.login_as_customer()
    catalog_flow.open_catalog()
    catalog_flow.add_multiple_books_to_cart(3)
    
    yield page
