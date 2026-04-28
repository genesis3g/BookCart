"""
Cliente para llamadas directas a la API REST de BookCart.
Usado principalmente en fixtures de setup/teardown para no depender del UI.
"""
import json
import urllib.request
import urllib.error
from utils.logger import logger


class ApiClient:
    """Llama a la API de BookCart sin pasar por el browser"""

    def __init__(self, base_url: str):
        self.base_url = base_url

    def login(self, username: str, password: str) -> dict:
        """POST /api/Login → devuelve { token, userDetails: { userId, ... } }"""
        payload = json.dumps({"username": username, "password": password}).encode()
        req = urllib.request.Request(
            f"{self.base_url}/api/Login",
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())

    def clear_cart(self, user_id: int) -> None:
        """DELETE /api/ShoppingCart/{userId} — no requiere autenticación"""
        req = urllib.request.Request(
            f"{self.base_url}/api/ShoppingCart/{user_id}",
            method="DELETE",
        )
        urllib.request.urlopen(req).close()

    def clear_wishlist(self, user_id: int, token: str) -> None:
        """DELETE /api/Wishlist/{userId} — requiere Bearer token"""
        req = urllib.request.Request(
            f"{self.base_url}/api/Wishlist/{user_id}",
            headers={"Authorization": f"Bearer {token}"},
            method="DELETE",
        )
        urllib.request.urlopen(req).close()

    def clean_user_state(self, username: str, password: str) -> None:
        """Login vía API + limpia carrito y wishlist del usuario"""
        logger.info(f"→ Limpiando estado para usuario: {username}")
        result = self.login(username, password)
        token = result["token"]
        user_id = result["userDetails"]["userId"]
        self.clear_cart(user_id)
        self.clear_wishlist(user_id, token)
        logger.info(f"✓ Carrito y wishlist limpios para: {username}")
