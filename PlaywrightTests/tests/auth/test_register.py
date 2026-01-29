import time
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from data.users import User, new_user
import random

# Genera un nombre y apellido aleatorio
def random_name():
    first_names = ["Namjoon", "Jin", "Yoongi", "Hoseok", "Jimin", "Taehyung", "Jungkook", "Gabriella", "Philipp", "Jonas"]
    last_names = ["Kim", "Min", "Jung", "Park", "Jeon", "Garcia", "Oksche", "Stautz", "BTS", "ARMY"]
    return random.choice(first_names), random.choice(last_names)

# Inserta un username limitado a max_length caracteres
def limit_length(s, max_length):
    """Limita el largo de una cadena a max_length caracteres"""
    return s[:max_length]

# Selecciona un genero random
def random_gender():
    return random.choice(["male", "female"])

# Verifica que la página de registro carga correctamente
def test_register_page_loads(page, base_url):
    """Test: Verifica que la página de registro carga correctamente"""
    register_page = RegisterPage(page, base_url)
    register_page.open()
    register_page.assert_loaded()
    
    # Verificar que todos los campos están visibles
    assert register_page.first_name_input.is_visible()
    assert register_page.last_name_input.is_visible()
    assert register_page.username_input.is_visible()
    assert register_page.password_input.is_visible()
    assert register_page.confirm_password_input.is_visible()

"""
Tests de registro de usuarios
"""

# Registrar un nuevo usuario exitosamente
def test_register_new_user(page, base_url):
    # Listener de consola para capturar errores JS
    page.on("console", lambda msg: print(f"CONSOLE [{msg.type}]: {msg.text}"))
    """Test: Registrar un nuevo usuario exitosamente"""
    max_username_length = 20  # Ajusta según el modelo de tu base de datos
    prefix = "testuser_"
    unique_id = str(int(time.time() * 1000))[-6:]
    username = limit_length(prefix + unique_id, max_username_length)
    print(f"Username generado: {username} (largo: {len(username)})")
    user = new_user()
    # Abrir página de registro
    register_page = RegisterPage(page, base_url)
    register_page.open()
    register_page.assert_loaded()
    # Interceptar la petición de registro
    registration_response = None
    def handle_response(response):
        nonlocal registration_response
        if "/api/user/register" in response.url:
            registration_response = response
    page.on("response", handle_response)
    # Registrar (llenar campos y seleccionar género)
    gender = random_gender()
    first_name, last_name = random_name()
    register_page.register(user, first_name=first_name, last_name=last_name, gender=gender)
    # Forzar submit real del formulario usando JS
    try:
        form = page.locator('form')
        if form.count() > 0:
            print("Forzando submit real del formulario con JS...")
            form.evaluate("form => form.submit()")
    except Exception as e:
        print(f"Error al forzar submit: {e}")
    time.sleep(2)
    print(f"URL después del registro: {page.url}")
    if registration_response:
        print(f"Status de registro: {registration_response.status}")
        try:
            print(f"Body: {registration_response.json()}")
        except Exception:
            print(f"Body (texto): {registration_response.text()}")
    else:
        print("No se capturó respuesta de registro.")
    # Mostrar errores visibles
    if register_page.error_messages.count() > 0:
        for i in range(register_page.error_messages.count()):
            print(f"Error {i+1}: {register_page.error_messages.nth(i).text_content()}")
    else:
        print("No hay errores visibles")
    # Diagnóstico visual y HTML
    html = page.content()
    print("\n=== HTML actual tras submit ===\n", html[:2000], "...\n[truncado]...")
    page.screenshot(path="register_debug.png")
    # Debería ser exitoso (redirigir)
    register_page.assert_registration_success()


# Registrar usuario y luego loguear con el mismo usuario
def test_register_then_login(page, base_url):
    """Test: Registrar usuario y luego loguear con el mismo usuario"""
    max_username_length = 20
    prefix = "testuser_"
    unique_id = str(int(time.time() * 1000))[-6:]
    username = limit_length(prefix + unique_id, max_username_length)
    print(f"Username generado: {username} (largo: {len(username)})")
    user = new_user()
    
    # 1) Registrar
    register_page = RegisterPage(page, base_url)
    register_page.open()
    gender = random_gender()
    first_name, last_name = random_name()
    register_page.register(user, first_name=first_name, last_name=last_name, gender=gender)
    register_page.assert_registration_success()
    
    # 2) Loguear con el mismo usuario
    login_page = LoginPage(page, base_url)
    login_page.open()
    login_page.login(user)
    login_page.assert_logged_in()


# Intentar registrar con un username que ya existe
def test_register_duplicate_username(page, base_url):
    """Test: Intenta registrar con un username que ya existe (debe fallar)"""
    # Usar un usuario que ya existe en la BD
    existing_user = User(
        username="playwright",
        password="SomeOtherPass123!"
    )
    
    register_page = RegisterPage(page, base_url)
    register_page.open()
    register_page.register(existing_user, first_name="Kim", last_name="Taehyung")
    
    # Debería fallar porque el usuario ya existe
    # Podría mostrar error o seguir en la página de registro
    assert page.url == f"{base_url}/register" or \
           register_page.error_messages.count() > 0


# Intentar registrar con una contraseña débil
def test_register_weak_password(page, base_url):
    """Test: Intenta registrar con contraseña débil (debe fallar)"""
    max_username_length = 20
    prefix = "user_"
    unique_id = str(int(time.time() * 1000))[-6:]
    username = limit_length(prefix + unique_id, max_username_length)
    print(f"Username generado: {username} (largo: {len(username)})")
    user = new_user()
    weak_password_user = User(
        username=user.username,
        password="weak"  # Contraseña demasiado corta
        )
    
    register_page = RegisterPage(page, base_url)
    register_page.open()
    gender = random_gender()
    first_name, last_name = random_name()
    register_page.register(weak_password_user, first_name=first_name, last_name=last_name, gender=gender)
    
    # Debería fallar (error de validación de contraseña)
    # Validar que sigue en la página o que hay errores
    assert page.url == f"{base_url}/register" or \
           register_page.error_messages.count() > 0


# Intentar registrar con un username demasiado largo
def test_register_too_long_username(page, base_url):
    """Test: Intenta registrar un usuario con username demasiado largo (debe fallar)"""
    # Username de 40 caracteres
    long_username = "x" * 40
    new_user = User(
        username=long_username,
        password="TestPass123!"
    )
    register_page = RegisterPage(page, base_url)
    register_page.open()
    register_page.first_name_input.fill("Jeon")
    register_page.last_name_input.fill("Jungkook")
    register_page.username_input.fill(new_user.username)
    register_page.password_input.fill(new_user.password)
    register_page.confirm_password_input.fill(new_user.password)
    # Seleccionar género
    gender_radios = register_page.gender_select
    for i in range(gender_radios.count()):
        radio = gender_radios.nth(i)
        value = radio.get_attribute("value")
        if value and value.lower() == "male":
            radio.click()
    # Enviar el formulario
    register_page.confirm_password_input.press("Enter")
    import time
    time.sleep(2)
    # Verificar que hay error visible o sigue en /register
    assert page.url == f"{base_url}/register" or register_page.error_messages.count() > 0
    