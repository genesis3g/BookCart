"""
Documentación de la nueva estructura de tests escalable
================================

## Estructura de directorios

PlaywrightTests/
├── config/                  # Configuración centralizada
│   └── settings.py         # Ambientes, rutas, configuración
│
├── data/                    # Datos de test
│   ├── users.py            # Definición de usuarios
│   └── test_data_builder.py # Factory para datos reutilizables
│
├── pages/                   # Page Objects
│   ├── base_page.py         # Clase base con métodos comunes
│   ├── common_page.py       # Componentes comunes (header, etc)
│   ├── home_page.py         # Página de inicio
│   ├── auth/                # Page objects de autenticación
│   └── catalog/             # Page objects de catálogo
│
├── flows/                   # Flujos reutilizables
│   ├── auth_flow.py         # Login, register, logout
│   ├── catalog_flow.py      # Búsqueda, filtros, carrito
│   └── order_flow.py        # Checkout y pedidos
│
├── fixtures/                # Fixtures avanzados
│   └── __init__.py
│
├── utils/                   # Utilidades
│   ├── logger.py            # Logging centralizado
│   ├── assertions.py        # Assertions personalizadas
│   ├── waits.py             # Esperas customizadas
│   └── helpers.py           # Helpers generales
│
├── tests/                   # Tests
│   ├── conftest.py          # Fixtures de tests
│   ├── auth/                # Tests de autenticación
│   ├── catalog/             # Tests de catálogo
│   ├── orders/              # Tests de órdenes
│   └── e2e/                 # Tests end-to-end
│
└── reports/                 # Reportes y artefactos
    ├── screenshots/
    └── logs/


## Ventajas de esta arquitectura

1. **Mantenibilidad**: Cambios en selectores en un solo lugar
2. **Reutilización**: Flows compartibles entre tests
3. **Escalabilidad**: Fácil agregar nuevos tests
4. **Claridad**: Tests más legibles y enfocados
5. **Debugging**: Logging automático y screenshots
6. **CI/CD**: Configuración por ambiente


## Cómo usar los Flows

### Login básico
```python
def test_login(auth_flow):
    auth_flow.login_as_customer()
```

### Compra completa
```python
def test_purchase(auth_flow, catalog_flow, order_flow):
    auth_flow.login_as_customer()
    catalog_flow.open_catalog().add_multiple_books_to_cart(3)
    order_flow.complete_purchase(address="123 St", city="City", zip_code="12345")
```

### Usando Page Objects directamente
```python
def test_home_page(page, base_url):
    home = HomePage(page, base_url)
    home.go()
    home.add_random_book_to_cart()
    home.assert_element_visible("[data-testid='cart-icon']")
```


## Configuration por Ambiente

Configurar con variables de entorno:
```bash
# Desarrollo
export TEST_ENV=dev
export BASE_URL=http://localhost:4200
export HEADLESS=false
export SLOW_MO=100

# Staging
export TEST_ENV=staging
export BASE_URL=https://staging.bookcart.com
export HEADLESS=true

# Producción
export TEST_ENV=prod
export BASE_URL=https://bookcart.com
export HEADLESS=true
```

O modificar `config/settings.py` directamente.


## Ejecutar tests

```bash
# Todos los tests
pytest

# Solo auth
pytest tests/auth/

# Con logging
pytest tests/auth/test_login.py -v --log-cli-level=DEBUG

# Con screenshot en fallos
pytest tests/auth/ -v  # Automático si SCREENSHOT_ON_FAILURE=True

# En paralelo (requiere pytest-xdist)
pytest tests/ -n auto
```


## Mejores prácticas

1. **Use Flows**: Para secuencias comunes de acciones
2. **Use Page Objects**: Para encapsular selectores y lógica de página
3. **Use Logger**: Para debugging y auditoría
4. **Use Fixtures**: Para setup/teardown compartido
5. **Use Test Data Builder**: Para crear datos reutilizables
6. **Chain Methods**: Retornar 'self' para fluencias
7. **Assertions en POs**: Incluir assertions en page objects


## Agregar un nuevo test

1. Crear el archivo: `tests/module/test_feature.py`
2. Importar flows/page objects necesarios
3. Usar fixtures o crear instancias manualmente
4. Escribir test encadenado usando flows

```python
def test_new_feature(auth_flow, catalog_flow):
    auth_flow.login_as_customer()
    catalog_flow.open_catalog()
    # ... más acciones
```


## Monitoreo y Reportes

Los logs se guardan en: `reports/logs/test_*.log`
Los screenshots se guardan en: `reports/screenshots/`

Se toman automáticamente en fallos si `SCREENSHOT_ON_FAILURE=True`
"""
