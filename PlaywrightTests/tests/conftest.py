"""
Configuración específica para tests
Aquí puedes agregar fixtures personalizadas por suite de tests
"""
import pytest
from flows.auth_flow import AuthFlow
from flows.catalog_flow import CatalogFlow
from flows.order_flow import OrderFlow
from utils.api_client import ApiClient
from data.test_data_builder import TestDataBuilder


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
def clean_test_users(base_url):
    """Limpia carrito y wishlist de los usuarios de prueba vía API antes del test.

    Usar como parámetro en tests que necesiten estado limpio:
        def test_foo(page, base_url, clean_test_users): ...
    """
    client = ApiClient(base_url)
    for role in ("customer", "customer_quemolle"):
        user = TestDataBuilder.get_test_user(role)
        client.clean_user_state(user.username, user.password)


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
