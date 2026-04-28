"""
Core Automation Flow — Demo Final
Cubre las directrices del proyecto de punta a punta:
  Home → Register → Login → Home (logged in) → Book Detail → Cart → Checkout → My Orders
"""
import pytest
from playwright.sync_api import expect
from flows.auth_flow import AuthFlow
from flows.catalog_flow import CatalogFlow
from flows.order_flow import OrderFlow


class TestCoreDemoFlow:
    """Flujo E2E completo según directrices del proyecto"""

    def test_core_demo_flow(self, page, base_url, clean_test_users):
        auth = AuthFlow(page, base_url)
        catalog = CatalogFlow(page, base_url)
        order = OrderFlow(page, base_url)

        # 1. Home Page — verificar que hay libros en el catálogo
        catalog.open_catalog()
        expect(page.locator("app-book-card").first).to_be_visible()

        # 2. Profile Icon / sección de usuario — navegar a login desde navbar
        page.get_by_role("button", name="Login").click()
        page.wait_for_url("**/login**")

        # 3. Registration — crear un usuario nuevo desde la página de login
        page.get_by_role("button", name="Register").click()
        page.wait_for_url("**/register**")
        auth.register_new_user()
        new_user = auth.get_last_registered_user()

        # 4. Login — usar las credenciales recién creadas
        auth.login_with_user(new_user)

        # 5. Home Page Return — verificar que el username aparece en el navbar
        catalog.open_catalog()
        expect(page.locator("mat-toolbar").get_by_text(new_user.username)).to_be_visible()

        # 6. Seleccionar producto — abrir la página de detalle del primer libro
        catalog.open_book_detail()
        expect(page.locator("mat-card-title", has_text="Book Details")).to_be_visible()

        # 7. Add to Cart — agregar el libro desde la página de detalle
        catalog.add_to_cart_from_detail()

        # 8. Proceed to Checkout — carrito → checkout
        order.go_to_cart()
        order.proceed_to_checkout()

        # 9. Payment / Shipping — completar el formulario de envío
        order.fill_shipping_info(
            name=new_user.username,
            address1="123 Test Street",
            address2="Apt 1",
            pincode="123456",
            state="Test State",
        )

        # 10. Confirmación — Place Order y verificar My Orders
        order.place_order()
        order.verify_order_confirmation()
