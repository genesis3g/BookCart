# PlaywrightTests/data/users.py
from dataclasses import dataclass

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
