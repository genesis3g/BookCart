# Generador de usuario único para tests
import time
from dataclasses import dataclass
from typing import Optional


def limit_length(s: str, max_length: int) -> str:
    """Limita la longitud de una cadena"""
    return s[:max_length]


def new_user() -> "User":
    """Genera un nuevo usuario único con timestamp"""
    max_username_length = 20
    prefix = "testuser_"
    unique_id = str(int(time.time() * 1000))[-6:]
    username = limit_length(prefix + unique_id, max_username_length)
    return User(username=username, password="TestPass123!")


@dataclass
class User:
    """Clase para representar un usuario de prueba"""
    username: str
    password: str


# Usuarios válidos en la base de datos
PLAYWRIGHT_USER = User(
    username="playwright",
    password="pw123!",
)

QUEMOLLE_USER = User(
    username="quemolle",
    password="Qwerty123456",
)


def existing_user() -> User:
    """Devuelve un usuario existente para los tests"""
    return PLAYWRIGHT_USER
