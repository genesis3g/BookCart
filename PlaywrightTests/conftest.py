"""
Configuración y fixtures de pytest para Playwright
"""
import sys
import os
import pytest
from pathlib import Path
from playwright.sync_api import sync_playwright

# Agregar el directorio de PlaywrightTests al path de Python
sys.path.insert(0, str(Path(__file__).parent))

from config.settings import BASE_URL, HEADLESS, SLOW_MO, SCREENSHOT_ON_FAILURE, SCREENSHOTS_DIR
from utils.logger import logger


@pytest.fixture(scope="session")
def base_url():
    """URL base de la aplicación"""
    logger.info(f"Base URL configurada: {BASE_URL}")
    return BASE_URL


@pytest.fixture(scope="session")
def browser_config():
    """Configuración del navegador"""
    return {
        "headless": HEADLESS,
        "slow_mo": SLOW_MO,
    }


@pytest.fixture(scope="session")
def playwright_instance(browser_config):
    """Crea una instancia de Playwright para la sesión"""
    logger.info("Iniciando Playwright...")
    playwright = sync_playwright().start()
    yield playwright
    logger.info("Cerrando Playwright...")
    playwright.stop()


@pytest.fixture(scope="session")
def browser(playwright_instance, browser_config):
    """Crea una instancia del navegador para la sesión"""
    logger.info(f"Lanzando navegador con config: {browser_config}")
    browser = playwright_instance.chromium.launch(**browser_config)
    yield browser
    logger.info("Cerrando navegador...")
    browser.close()


@pytest.fixture(scope="function")
def context(browser):
    """Crea un contexto del navegador para cada test"""
    logger.debug("Creando contexto del navegador...")
    context = browser.new_context()
    yield context
    logger.debug("Cerrando contexto del navegador...")
    context.close()


@pytest.fixture(scope="function")
def page(context, request):
    """Crea una página del navegador para cada test"""
    logger.debug(f"Creando página para test: {request.node.name}")
    page = context.new_page()
    
    yield page
    
    # Capturar screenshot si hay fallo
    if request.node.rep_call.failed and SCREENSHOT_ON_FAILURE:
        screenshot_name = f"failed_{request.node.name}"
        screenshot_path = os.path.join(SCREENSHOTS_DIR, f"{screenshot_name}.png")
        page.screenshot(path=screenshot_path)
        logger.error(f"Test fallido. Screenshot guardado: {screenshot_path}")
    
    logger.debug("Cerrando página...")
    page.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook para capturar información de tests fallidos"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
