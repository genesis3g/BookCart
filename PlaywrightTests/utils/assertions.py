"""
Assertions customizadas para tests de Playwright
"""
from typing import Any
from utils.logger import logger


class AssertionError(Exception):
    """Excepción personalizada para assertions"""
    pass


def assert_element_visible(selector: str, page) -> None:
    """
    Verifica que un elemento sea visible en la página
    
    Args:
        selector: Selector del elemento
        page: Objeto página de Playwright
    
    Raises:
        AssertionError: Si el elemento no es visible
    """
    try:
        element = page.query_selector(selector)
        if not element or not element.is_visible():
            logger.error(f"Elemento no visible: {selector}")
            raise AssertionError(f"Elemento '{selector}' no es visible")
        logger.debug(f"Elemento visible: {selector}")
    except Exception as e:
        logger.error(f"Error al verificar elemento visible: {e}")
        raise


def assert_text_present(text: str, page) -> None:
    """
    Verifica que un texto esté presente en la página
    
    Args:
        text: Texto a buscar
        page: Objeto página de Playwright
    
    Raises:
        AssertionError: Si el texto no está presente
    """
    page_text = page.content()
    if text not in page_text:
        logger.error(f"Texto no encontrado: '{text}'")
        raise AssertionError(f"Texto '{text}' no encontrado en la página")
    logger.debug(f"Texto encontrado: '{text}'")


def assert_url_contains(url_part: str, page) -> None:
    """
    Verifica que la URL contenga cierta parte
    
    Args:
        url_part: Parte de la URL a buscar
        page: Objeto página de Playwright
    
    Raises:
        AssertionError: Si la URL no contiene el fragmento
    """
    current_url = page.url
    if url_part not in current_url:
        logger.error(f"URL no contiene: '{url_part}'. URL actual: {current_url}")
        raise AssertionError(f"URL no contiene '{url_part}'")
    logger.debug(f"URL contiene: '{url_part}'")


def assert_element_count(selector: str, expected_count: int, page) -> None:
    """
    Verifica que el número de elementos coincida con lo esperado
    
    Args:
        selector: Selector de elementos
        expected_count: Número esperado de elementos
        page: Objeto página de Playwright
    
    Raises:
        AssertionError: Si el conteo no coincide
    """
    elements = page.query_selector_all(selector)
    actual_count = len(elements)
    
    if actual_count != expected_count:
        logger.error(
            f"Conteo de elementos no coincide. "
            f"Esperado: {expected_count}, Actual: {actual_count}. "
            f"Selector: {selector}"
        )
        raise AssertionError(
            f"Esperaba {expected_count} elementos, se encontraron {actual_count}"
        )
    logger.debug(f"Conteo correcto: {actual_count} elementos")


def assert_value_equals(actual: Any, expected: Any, message: str = "") -> None:
    """
    Verifica que un valor sea igual al esperado
    
    Args:
        actual: Valor actual
        expected: Valor esperado
        message: Mensaje adicional
    
    Raises:
        AssertionError: Si los valores no coinciden
    """
    if actual != expected:
        error_msg = f"Esperado '{expected}', pero se obtuvo '{actual}'"
        if message:
            error_msg = f"{error_msg}. {message}"
        logger.error(error_msg)
        raise AssertionError(error_msg)
    logger.debug(f"Valores coinciden: {expected}")
