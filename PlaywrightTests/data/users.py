# Generador de usuario único para tests
import time
# PlaywrightTests/data/users.py
from dataclasses import dataclass


def limit_length(s, max_length):
    return s[:max_length]

def new_user():
    max_username_length = 20
    prefix = "testuser_"
    unique_id = str(int(time.time() * 1000))[-6:]
    username = limit_length(prefix + unique_id, max_username_length)
    return User(username=username, password="TestPass123!")

@dataclass
class User:
    username: str
    password: str

# Usuarios válidos en la BD
PLAYWRIGHT_USER = User(
    username="playwright",
    password="pw123!",
)

QUEMOLLE_USER = User(
    username="quemolle",
    password="Qwerty123456",
)

def existing_user():
    # Devuelve un usuario existente para los tests
    return PLAYWRIGHT_USER
