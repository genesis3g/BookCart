import random
import string
from typing import TypedDict


class UserData(TypedDict):
    first_name: str
    last_name: str
    username: str
    password: str
    gender: str


# Fixed user for ad-hoc and exploratory tests.
# This user must exist in the database before running the suite.
PLAYWRIGHT_USER: UserData = {
    "first_name": "Playwright",
    "last_name": "Tester",
    "username": "playwright",
    "password": "Playwright1",
    "gender": "Male",
}


def random_username(length: int = 8) -> str:
    suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return f"user_{suffix}"


def random_password() -> str:
    # Satisfies backend regex: ^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$
    return f"Test{random.randint(100, 999)}Pw"


def random_user() -> UserData:
    return {
        "first_name": "Test",
        "last_name": "User",
        "username": random_username(),
        "password": random_password(),
        "gender": random.choice(["Male", "Female"]),
    }
