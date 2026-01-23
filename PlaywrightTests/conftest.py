"""
Configuración y fixtures de pytest para Playwright
"""
import sys
import pytest
import os
from pathlib import Path

# Agregar el directorio de PlaywrightTests al path de Python
sys.path.insert(0, str(Path(__file__).parent))

from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def base_url():
    """URL base de la aplicación"""
    return os.getenv("BASE_URL", "http://localhost:4200")


@pytest.fixture
def browser():
    """Crea una instancia del navegador para cada test"""
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, slow_mo=100)
    yield browser
    browser.close()
    playwright.stop()


@pytest.fixture
def context(browser):
    """Crea un contexto del navegador para cada test"""
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture
def page(context):
    """Crea una página del navegador para cada test"""
    page = context.new_page()
    yield page
    page.close()
