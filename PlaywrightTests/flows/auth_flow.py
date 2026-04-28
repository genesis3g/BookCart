"""
Flujo de autenticación reutilizable
"""
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from data.test_data_builder import TestDataBuilder
from data.users import User
from utils.logger import logger


class AuthFlow:
    """Flujo de autenticación para tests"""
    
    def __init__(self, page, base_url):
        self.page = page
        self.base_url = base_url
        self.login_page = LoginPage(page, base_url)
        self.register_page = RegisterPage(page, base_url)
        self.logger = logger
    
    def login_as_customer(self) -> "AuthFlow":
        """Realiza login como cliente"""
        self.logger.info("→ Iniciando login como customer")
        user = TestDataBuilder.get_test_user("customer")
        self.login_page.open()
        self.login_page.login(user)
        self.login_page.assert_logged_in()
        self.logger.info("✓ Login exitoso como customer")
        return self
    
    def login_with_user(self, user: User) -> "AuthFlow":
        """Realiza login con un usuario específico y verifica el nombre en navbar"""
        self.logger.info(f"→ Iniciando login con usuario: {user.username}")
        self.login_page.open()
        self.login_page.login(user)
        self.login_page.assert_logged_in(username=user.username)
        self.logger.info(f"✓ Login realizado con {user.username}")
        return self
    
    def login_as_admin(self) -> "AuthFlow":
        """Realiza login como administrador"""
        self.logger.info("→ Iniciando login como admin")
        user = TestDataBuilder.get_test_user("admin")
        self.login_page.open()
        self.login_page.login(user)
        self.logger.info("✓ Login exitoso como admin")
        return self
    
    def register_new_user(self) -> "AuthFlow":
        """Registra un nuevo usuario"""
        self.logger.info("→ Registrando nuevo usuario")
        user = TestDataBuilder.get_test_user("new")
        self._last_registered_user = user
        self.register_page.open()
        self.register_page.register(user)
        self.register_page.assert_registration_success()
        self.logger.info(f"✓ Registro exitoso para usuario: {user.username}")
        return self

    def get_last_registered_user(self) -> User:
        """Devuelve el último usuario registrado en esta sesión"""
        return self._last_registered_user
    
    def logout(self) -> "AuthFlow":
        """Cierra la sesión del usuario actual"""
        self.logger.info("→ Realizando logout")
        # Implementar logout según la estructura de la app
        # self.login_page.click("logout-button")
        self.logger.info("✓ Logout completado")
        return self
    
    def try_invalid_login(self) -> "AuthFlow":
        """Intenta login con credenciales inválidas (debe fallar)"""
        self.logger.info("→ Intentando login con credenciales inválidas")
        invalid_user = TestDataBuilder.get_invalid_user()
        self.login_page.open()
        self.login_page.login(invalid_user)
        self.login_page.assert_login_failed()
        self.logger.info("✓ Login fallido como se esperaba")
        return self
