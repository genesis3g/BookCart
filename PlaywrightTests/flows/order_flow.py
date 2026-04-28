"""
Flujo de pedidos y checkout
"""
import re
from playwright.sync_api import expect
from utils.logger import logger


class OrderFlow:
    """Flujo para realizar pedidos y checkout"""

    def __init__(self, page, base_url):
        self.page = page
        self.base_url = base_url
        self.logger = logger

    def go_to_cart(self) -> "OrderFlow":
        """Navega al carrito de compras"""
        self.logger.info("→ Navegando al carrito")
        self.page.goto(f"{self.base_url}/shopping-cart")
        self.page.wait_for_load_state("networkidle")
        expect(self.page.locator("mat-card-title", has_text="Shopping cart")).to_be_visible()
        self.logger.info("✓ Carrito abierto")
        return self

    def proceed_to_checkout(self) -> "OrderFlow":
        """Procede al checkout desde el carrito"""
        self.logger.info("→ Procediendo a checkout")
        self.page.get_by_role("button", name="CheckOut").click()
        self.page.wait_for_url("**/checkout**")
        self.logger.info("✓ En página de checkout")
        return self

    def fill_shipping_info(
        self,
        name: str,
        address1: str,
        address2: str,
        pincode: str,
        state: str,
    ) -> "OrderFlow":
        """Completa el formulario de envío del checkout"""
        self.logger.info(f"→ Ingresando datos de envío para: {name}")
        self.page.locator('input[formcontrolname="name"]').fill(name)
        self.page.locator('input[formcontrolname="addressLine1"]').fill(address1)
        self.page.locator('input[formcontrolname="addressLine2"]').fill(address2)
        self.page.locator('input[formcontrolname="pincode"]').fill(pincode)
        self.page.locator('input[formcontrolname="state"]').fill(state)
        self.logger.info("✓ Información de envío completada")
        return self

    def place_order(self) -> "OrderFlow":
        """Envía el formulario y realiza el pedido"""
        self.logger.info("→ Confirmando pedido")
        self.page.get_by_role("button", name="Place Order").click()
        self.page.wait_for_url("**/myorders**")
        self.logger.info("✓ Pedido realizado")
        return self

    def verify_order_confirmation(self) -> "OrderFlow":
        """Verifica que se aterrizó en la página de Mis Órdenes"""
        self.logger.info("→ Verificando confirmación de pedido")
        expect(self.page).to_have_url(re.compile(r"/myorders", re.I))
        expect(self.page.locator("mat-card-title", has_text="My Orders")).to_be_visible()
        self.logger.info("✓ Pedido confirmado correctamente")
        return self

    def complete_purchase(
        self,
        name: str = "Test User",
        address1: str = "123 Test Street",
        address2: str = "Apt 1",
        pincode: str = "123456",
        state: str = "Test State",
    ) -> "OrderFlow":
        """Completa todo el flujo de compra"""
        self.logger.info("→ Iniciando flujo completo de compra")
        self.go_to_cart()
        self.proceed_to_checkout()
        self.fill_shipping_info(name, address1, address2, pincode, state)
        self.place_order()
        self.verify_order_confirmation()
        self.logger.info("✓ Compra completada exitosamente")
        return self
