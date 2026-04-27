"""
Page Object mejorado con métodos reutilizables
"""
from playwright.sync_api import Page
from config.settings import BASE_URL, TIMEOUT
from utils.logger import logger


class BasePage:
    """Clase base para todos los Page Objects"""
    
    def __init__(self, page: Page, base_url: str = BASE_URL):
        self.page = page
        self.base_url = base_url
        self.logger = logger
    
    # ===== NAVEGACIÓN =====
    
    def goto(self, path: str = ""):
        """Navega a una URL relativa o absoluta"""
        full_url = f"{self.base_url}{path}"
        self.logger.info(f"Navegando a: {full_url}")
        self.page.goto(full_url)
        return self
    
    def wait_for_load(self, timeout: int = TIMEOUT):
        """Espera a que la página cargue completamente"""
        self.logger.debug("Esperando carga de página...")
        self.page.wait_for_load_state("networkidle", timeout=timeout)
        return self
    
    def reload(self):
        """Recarga la página actual"""
        self.logger.info("Recargando página...")
        self.page.reload()
        return self
    
    def go_back(self):
        """Va a la página anterior"""
        self.logger.info("Volviendo a página anterior...")
        self.page.go_back()
        return self
    
    # ===== LOCALIZADOR DE ELEMENTOS =====
    
    def get_element(self, selector: str):
        """Obtiene un elemento por selector"""
        return self.page.query_selector(selector)
    
    def get_elements(self, selector: str):
        """Obtiene todos los elementos que coincidan con el selector"""
        return self.page.query_selector_all(selector)
    
    def element_exists(self, selector: str) -> bool:
        """Verifica si un elemento existe"""
        return self.page.query_selector(selector) is not None
    
    def element_is_visible(self, selector: str) -> bool:
        """Verifica si un elemento es visible"""
        element = self.get_element(selector)
        return element and element.is_visible() if element else False
    
    # ===== INTERACCIÓN CON ELEMENTOS =====
    
    def click(self, selector: str, timeout: int = TIMEOUT):
        """Hace click en un elemento"""
        self.logger.debug(f"Click en: {selector}")
        self.page.click(selector, timeout=timeout)
        return self
    
    def double_click(self, selector: str):
        """Hace doble click en un elemento"""
        self.logger.debug(f"Doble click en: {selector}")
        self.page.dblclick(selector)
        return self
    
    def right_click(self, selector: str):
        """Hace click derecho en un elemento"""
        self.logger.debug(f"Click derecho en: {selector}")
        self.page.right_click(selector)
        return self
    
    def fill(self, selector: str, text: str):
        """Rellena un campo de texto"""
        self.logger.debug(f"Rellenando {selector} con: {text}")
        self.page.fill(selector, text)
        return self
    
    def clear(self, selector: str):
        """Limpia el contenido de un campo"""
        self.logger.debug(f"Limpiando: {selector}")
        self.page.fill(selector, "")
        return self
    
    def type_text(self, selector: str, text: str, delay: int = 50):
        """Escribe texto carácter por carácter"""
        self.logger.debug(f"Escribiendo en {selector}: {text}")
        self.page.type(selector, text, delay=delay)
        return self
    
    def press_key(self, selector: str, key: str):
        """Presiona una tecla en un elemento"""
        self.logger.debug(f"Presionando {key} en: {selector}")
        self.page.press(selector, key)
        return self
    
    def select_option(self, selector: str, value: str):
        """Selecciona una opción en un dropdown"""
        self.logger.debug(f"Seleccionando {value} en: {selector}")
        self.page.select_option(selector, value)
        return self
    
    # ===== OBTENER INFORMACIÓN =====
    
    def get_text(self, selector: str) -> str:
        """Obtiene el texto de un elemento"""
        text = self.page.text_content(selector)
        self.logger.debug(f"Texto obtenido de {selector}: {text}")
        return text
    
    def get_attribute(self, selector: str, attribute: str) -> str:
        """Obtiene el atributo de un elemento"""
        value = self.page.get_attribute(selector, attribute)
        self.logger.debug(f"Atributo {attribute} de {selector}: {value}")
        return value
    
    def get_input_value(self, selector: str) -> str:
        """Obtiene el valor de un input"""
        return self.page.input_value(selector)
    
    def get_current_url(self) -> str:
        """Obtiene la URL actual"""
        return self.page.url
    
    def get_title(self) -> str:
        """Obtiene el título de la página"""
        return self.page.title()
    
    # ===== ESPERAS =====
    
    def wait_for_element(self, selector: str, timeout: int = TIMEOUT):
        """Espera a que un elemento esté presente"""
        self.logger.debug(f"Esperando elemento: {selector}")
        self.page.wait_for_selector(selector, timeout=timeout)
        return self
    
    def wait_for_element_visible(self, selector: str, timeout: int = TIMEOUT):
        """Espera a que un elemento sea visible"""
        self.logger.debug(f"Esperando elemento visible: {selector}")
        self.page.locator(selector).wait_for(timeout=timeout, state="visible")
        return self
    
    def wait_for_element_hidden(self, selector: str, timeout: int = TIMEOUT):
        """Espera a que un elemento esté oculto"""
        self.logger.debug(f"Esperando elemento oculto: {selector}")
        self.page.locator(selector).wait_for(timeout=timeout, state="hidden")
        return self
    
    def wait_for_url(self, url_pattern: str, timeout: int = TIMEOUT):
        """Espera a que la URL contenga un patrón"""
        self.logger.debug(f"Esperando URL con patrón: {url_pattern}")
        self.page.wait_for_url(f"**{url_pattern}**", timeout=timeout)
        return self
    
    # ===== ASSERTIONS =====
    
    def assert_url_contains(self, url_part: str):
        """Verifica que la URL contiene una parte específica"""
        current_url = self.get_current_url()
        assert url_part in current_url, f"URL no contiene '{url_part}'. URL actual: {current_url}"
        self.logger.info(f"✓ URL contiene '{url_part}'")
        return self
    
    def assert_element_visible(self, selector: str):
        """Verifica que un elemento es visible"""
        assert self.element_is_visible(selector), f"Elemento '{selector}' no es visible"
        self.logger.info(f"✓ Elemento visible: {selector}")
        return self
    
    def assert_element_exists(self, selector: str):
        """Verifica que un elemento existe"""
        assert self.element_exists(selector), f"Elemento '{selector}' no existe"
        self.logger.info(f"✓ Elemento existe: {selector}")
        return self
    
    def assert_text_visible(self, text: str):
        """Verifica que un texto es visible en la página"""
        page_content = self.page.content()
        assert text in page_content, f"Texto '{text}' no encontrado en la página"
        self.logger.info(f"✓ Texto visible: '{text}'")
        return self
    
    def assert_element_text(self, selector: str, expected_text: str):
        """Verifica que el texto de un elemento coincide"""
        actual_text = self.get_text(selector)
        assert actual_text == expected_text, f"Esperado '{expected_text}', se obtuvo '{actual_text}'"
        self.logger.info(f"✓ Texto correcto en {selector}: '{expected_text}'")
        return self
    
    # ===== MANEJO DE SCREENSHOTS Y DEBUGGING =====
    
    def take_screenshot(self, name: str = "screenshot") -> str:
        """Toma una captura de pantalla"""
        from config.settings import SCREENSHOTS_DIR
        import os
        import time
        
        timestamp = int(time.time() * 1000)
        filename = f"{name}_{timestamp}.png"
        filepath = os.path.join(SCREENSHOTS_DIR, filename)
        
        self.page.screenshot(path=filepath)
        self.logger.info(f"Screenshot guardado: {filepath}")
        return filepath
    
    def switch_to_iframe(self, selector: str):
        """Cambia el contexto a un iframe"""
        self.logger.debug(f"Cambiando a iframe: {selector}")
        frame = self.page.frame_locator(selector)
        return frame
    
    def get_page_context(self):
        """Devuelve el contexto de la página para operaciones avanzadas"""
        return self.page
