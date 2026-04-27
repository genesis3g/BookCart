"""
Logger centralizado para tests de Playwright
"""
import logging
import os
from config.settings import LOGS_DIR, CURRENT_ENV


def setup_logger(name: str) -> logging.Logger:
    """
    Configura y retorna un logger con formato consistente
    
    Args:
        name: Nombre del logger (típicamente __name__)
    
    Returns:
        Logger configurado
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # Evitar duplicar handlers
    if logger.hasHandlers():
        return logger
    
    # Formato del log
    log_format = logging.Formatter(
        fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Handler para archivo
    log_file = os.path.join(LOGS_DIR, f"test_{CURRENT_ENV}.log")
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(log_format)
    
    # Handler para consola
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(log_format)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger


# Logger global para usar en fixtures y helpers
logger = setup_logger("bookcart_tests")
