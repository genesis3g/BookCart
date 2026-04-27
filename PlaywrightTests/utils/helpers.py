"""Utilidades y helpers generales para tests"""
import os
from datetime import datetime


def get_timestamp() -> str:
    """Obtiene timestamp actual en formato ISO"""
    return datetime.now().isoformat()


def get_test_report_path(filename: str) -> str:
    """Obtiene ruta para guardar reportes"""
    from config.settings import REPORTS_DIR
    return os.path.join(REPORTS_DIR, filename)


def ensure_directory_exists(directory_path: str) -> None:
    """Crea un directorio si no existe"""
    os.makedirs(directory_path, exist_ok=True)


def read_test_data_file(filename: str) -> str:
    """Lee un archivo de datos de test"""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "data", filename)
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Archivo de datos no encontrado: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def cleanup_screenshots_older_than(days: int = 7) -> None:
    """Limpia screenshots más antiguos que N días"""
    from config.settings import SCREENSHOTS_DIR
    import time
    
    current_time = time.time()
    seconds_in_day = 86400
    
    for filename in os.listdir(SCREENSHOTS_DIR):
        file_path = os.path.join(SCREENSHOTS_DIR, filename)
        if os.path.isfile(file_path):
            file_age = current_time - os.path.getmtime(file_path)
            if file_age > seconds_in_day * days:
                os.remove(file_path)
