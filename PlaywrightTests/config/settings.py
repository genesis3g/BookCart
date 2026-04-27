"""
Configuración centralizada para tests de Playwright
Soporta múltiples ambientes: dev, staging, prod
"""
import os
from enum import Enum
from typing import Dict, Any


class Environment(Enum):
    """Ambientes soportados"""
    DEV = "dev"
    STAGING = "staging"
    PROD = "prod"


# Detectar ambiente desde variable de entorno o usar dev por defecto
CURRENT_ENV = os.getenv("TEST_ENV", "dev").lower()

# Configuración por ambiente
ENVIRONMENT_CONFIG: Dict[str, Dict[str, Any]] = {
    "dev": {
        "base_url": os.getenv("BASE_URL", "http://localhost:4200"),
        "headless": os.getenv("HEADLESS", "false").lower() == "true",
        "slow_mo": int(os.getenv("SLOW_MO", "100")),
        "timeout": 30000,
        "screenshot_on_failure": True,
    },
    "staging": {
        "base_url": os.getenv("BASE_URL", "https://staging.bookcart.com"),
        "headless": os.getenv("HEADLESS", "true").lower() == "true",
        "slow_mo": int(os.getenv("SLOW_MO", "0")),
        "timeout": 60000,
        "screenshot_on_failure": True,
    },
    "prod": {
        "base_url": os.getenv("BASE_URL", "https://bookcart.com"),
        "headless": os.getenv("HEADLESS", "true").lower() == "true",
        "slow_mo": int(os.getenv("SLOW_MO", "0")),
        "timeout": 120000,
        "screenshot_on_failure": False,
    },
}

# Configuración activa
if CURRENT_ENV not in ENVIRONMENT_CONFIG:
    raise ValueError(f"Ambiente no válido: {CURRENT_ENV}. Use: dev, staging, prod")

SETTINGS = ENVIRONMENT_CONFIG[CURRENT_ENV]

# Variables de configuración globales
BASE_URL = SETTINGS["base_url"]
HEADLESS = SETTINGS["headless"]
SLOW_MO = SETTINGS["slow_mo"]
TIMEOUT = SETTINGS["timeout"]
SCREENSHOT_ON_FAILURE = SETTINGS["screenshot_on_failure"]

# Rutas de directorios
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
SCREENSHOTS_DIR = os.path.join(REPORTS_DIR, "screenshots")
LOGS_DIR = os.path.join(REPORTS_DIR, "logs")

# Crear directorios si no existen
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True)
