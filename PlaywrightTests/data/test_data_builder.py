"""
Factory pattern para construcción de datos de test
"""
from dataclasses import dataclass
from typing import Optional, Dict, Any
from data.users import User, new_user


@dataclass
class BookTestData:
    """Datos para testing de libros"""
    title: str
    author: str
    price: float
    category: str


@dataclass
class OrderTestData:
    """Datos para testing de órdenes"""
    customer_email: str
    total: float
    items_count: int
    address: str


class TestDataBuilder:
    """Factory para crear datos de test reutilizables"""
    
    @staticmethod
    def get_test_user(role: str = "customer") -> User:
        """
        Obtiene un usuario de prueba
        
        Args:
            role: Rol del usuario ('customer', 'admin', 'new')
        
        Returns:
            User object
        """
        users = {
            "customer": User(username="playwright", password="pw123!"),
            "customer_quemolle": User(username="quemolle", password="Qwerty123456"),
            "admin": User(username="admin", password="Admin@123"),
            "new": new_user(),
        }
        
        if role not in users:
            raise ValueError(f"Rol no válido: {role}")
        
        return users[role]
    
    @staticmethod
    def get_invalid_user() -> User:
        """Devuelve un usuario con credenciales inválidas"""
        return User(username="invalid_xyz_123", password="wrong_pass_456")
    
    @staticmethod
    def get_test_book() -> BookTestData:
        """Devuelve datos de un libro para testing"""
        return BookTestData(
            title="The Art of Testing",
            author="Test Author",
            price=29.99,
            category="Technology"
        )
    
    @staticmethod
    def get_multiple_test_books(count: int = 3) -> list[BookTestData]:
        """Devuelve múltiples libros para testing"""
        books = [
            BookTestData("Book One", "Author One", 19.99, "Fiction"),
            BookTestData("Book Two", "Author Two", 24.99, "Science"),
            BookTestData("Book Three", "Author Three", 29.99, "Technology"),
            BookTestData("Book Four", "Author Four", 34.99, "History"),
            BookTestData("Book Five", "Author Five", 14.99, "Romance"),
        ]
        return books[:count]
    
    @staticmethod
    def get_test_order() -> OrderTestData:
        """Devuelve datos de una orden para testing"""
        return OrderTestData(
            customer_email="test@example.com",
            total=99.97,
            items_count=3,
            address="123 Test St, Test City, TC 12345"
        )
    
    @staticmethod
    def get_valid_credentials() -> Dict[str, str]:
        """Devuelve credenciales válidas para login"""
        user = TestDataBuilder.get_test_user("customer")
        return {"username": user.username, "password": user.password}
    
    @staticmethod
    def get_invalid_credentials() -> Dict[str, str]:
        """Devuelve credenciales inválidas para login"""
        return {"username": "invalid@test.com", "password": "WrongPassword123"}
    
    @staticmethod
    def get_empty_credentials() -> Dict[str, str]:
        """Devuelve credenciales vacías para testing validación"""
        return {"username": "", "password": ""}
