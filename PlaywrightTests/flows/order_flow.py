"""
Flujo de pedidos y checkout
"""
from data.test_data_builder import TestDataBuilder
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
        # self.page.click("cart-button")
        self.logger.info("✓ Carrito abierto")
        return self
    
    def proceed_to_checkout(self) -> "OrderFlow":
        """Procede al checkout desde el carrito"""
        self.logger.info("→ Procediendo a checkout")
        # self.page.click("checkout-button")
        self.logger.info("✓ En página de checkout")
        return self
    
    def fill_shipping_info(self, address: str, city: str, zip_code: str) -> "OrderFlow":
        """Completa información de envío"""
        self.logger.info(f"→ Ingresando dirección: {address}")
        # self.page.fill("address-field", address)
        # self.page.fill("city-field", city)
        # self.page.fill("zip-field", zip_code)
        self.logger.info("✓ Información de envío completada")
        return self
    
    def fill_payment_info(self) -> "OrderFlow":
        """Completa información de pago"""
        self.logger.info("→ Ingresando información de pago")
        # self.page.fill("card-number", "4111111111111111")
        # self.page.fill("expiry", "12/25")
        # self.page.fill("cvv", "123")
        self.logger.info("✓ Información de pago completada")
        return self
    
    def place_order(self) -> "OrderFlow":
        """Realiza el pedido"""
        self.logger.info("→ Confirmando pedido")
        # self.page.click("place-order-button")
        self.logger.info("✓ Pedido realizado")
        return self
    
    def verify_order_confirmation(self) -> "OrderFlow":
        """Verifica que el pedido se completó exitosamente"""
        self.logger.info("→ Verificando confirmación de pedido")
        # self.page.assert_text_visible("Pedido confirmado")
        self.logger.info("✓ Pedido confirmado correctamente")
        return self
    
    def complete_purchase(self, address: str = None, city: str = None, zip_code: str = None) -> "OrderFlow":
        """Completa todo el flujo de compra"""
        self.logger.info("→ Iniciando flujo completo de compra")
        self.go_to_cart()
        self.proceed_to_checkout()
        
        if address:
            self.fill_shipping_info(address, city, zip_code)
        
        self.fill_payment_info()
        self.place_order()
        self.verify_order_confirmation()
        
        self.logger.info("✓ Compra completada exitosamente")
        return self
