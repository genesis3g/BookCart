"""
Custom waits y helpers para esperas en Playwright
"""
import time
from playwright.sync_api import Page
from utils.logger import logger


def wait_for_element_clickable(page: Page, selector: str, timeout: int = 5000) -> bool:
    """
    Espera hasta que un elemento sea clickeable
    
    Args:
        page: Objeto página de Playwright
        selector: Selector del elemento
        timeout: Timeout en milisegundos
    
    Returns:
        True si el elemento es clickeable, False en caso contrario
    """
    try:
        page.wait_for_selector(selector, timeout=timeout)
        element = page.query_selector(selector)
        
        start = time.time()
        while (time.time() - start) * 1000 < timeout:
            if element and element.is_visible() and element.is_enabled():
                logger.debug(f"Elemento clickeable: {selector}")
                return True
            time.sleep(0.1)
        
        logger.warning(f"Elemento no clickeable dentro del timeout: {selector}")
        return False
    except Exception as e:
        logger.error(f"Error esperando elemento clickeable: {e}")
        return False


def wait_for_navigation(page: Page, timeout: int = 30000) -> bool:
    """
    Espera a que se complete una navegación
    
    Args:
        page: Objeto página de Playwright
        timeout: Timeout en milisegundos
    
    Returns:
        True si la navegación se completó
    """
    try:
        page.wait_for_load_state("networkidle", timeout=timeout)
        logger.debug("Navegación completada")
        return True
    except Exception as e:
        logger.error(f"Error esperando navegación: {e}")
        return False


def wait_for_request(page: Page, pattern: str, timeout: int = 10000) -> bool:
    """
    Espera a que se realice una request específica
    
    Args:
        page: Objeto página de Playwright
        pattern: Patrón de URL a esperar
        timeout: Timeout en milisegundos
    
    Returns:
        True si la request se realizó
    """
    try:
        with page.expect_request(pattern, timeout=timeout) as request_context:
            request = request_context.value
        logger.debug(f"Request encontrada: {request.url}")
        return True
    except Exception as e:
        logger.warning(f"Request no encontrada: {pattern}. Error: {e}")
        return False


def wait_for_response(page: Page, pattern: str, timeout: int = 10000) -> bool:
    """
    Espera a que se reciba una response específica
    
    Args:
        page: Objeto página de Playwright
        pattern: Patrón de URL a esperar
        timeout: Timeout en milisegundos
    
    Returns:
        True si la response se recibió
    """
    try:
        with page.expect_response(pattern, timeout=timeout) as response_context:
            response = response_context.value
        logger.debug(f"Response recibida de: {response.url} ({response.status})")
        return True
    except Exception as e:
        logger.warning(f"Response no recibida: {pattern}. Error: {e}")
        return False
