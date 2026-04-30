import urllib3
import requests
from typing import Any

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class ApiClient:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.verify = False  # local dev uses self-signed certificate

    def _url(self, path: str) -> str:
        return f"{self.base_url}{path}"

    # --- Auth ---

    def login(self, username: str, password: str) -> dict[str, Any]:
        response = self.session.post(
            self._url("/api/login"),
            json={"username": username, "password": password},
        )
        response.raise_for_status()
        return response.json()

    def register(self, user: dict[str, Any]) -> dict[str, Any]:
        response = self.session.post(
            self._url("/api/user"),
            json={
                "firstName": user["first_name"],
                "lastName": user["last_name"],
                "userName": user["username"],
                "password": user["password"],
                "confirmPassword": user["password"],
                "gender": user["gender"],
            },
        )
        response.raise_for_status()
        return response.json()

    # --- Books ---

    def get_books(self) -> list[dict[str, Any]]:
        response = self.session.get(self._url("/api/book"))
        response.raise_for_status()
        return response.json()

    def get_book(self, book_id: int) -> dict[str, Any]:
        response = self.session.get(self._url(f"/api/book/{book_id}"))
        response.raise_for_status()
        return response.json()

    def get_categories(self) -> list[str]:
        response = self.session.get(self._url("/api/book/GetCategoriesList"))
        response.raise_for_status()
        return response.json()

    # --- Orders ---

    def get_orders(self, user_id: int) -> list[dict[str, Any]]:
        response = self.session.get(self._url(f"/api/order/{user_id}"))
        response.raise_for_status()
        return response.json()
