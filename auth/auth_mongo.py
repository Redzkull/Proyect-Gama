import re
from cone_mongo import get_db
from werkzeug.security import generate_password_hash, check_password_hash

# Función para validar el formato del correo
def validar_email(email):
    patron = r"(^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$)"
    return re.match(patron, email) is not None

# Verificar si el usuario existe por email
def verificar_usuario(email):
    db = get_db()
    usuario = db["usuarios"].find_one({"email": email})
    return usuario is not None

# Registrar un nuevo usuario
def registrar_usuario(email, password):
    db = get_db()
    hashed_password = generate_password_hash(password)
    db["usuarios"].insert_one({"email": email, "password": hashed_password})
    print(f"Usuario registrado exitosamente con email: {email}")

# Iniciar sesión del usuario
def iniciar_sesion(email, password):
    db = get_db()
    usuario = db["usuarios"].find_one({"email": email})
    if usuario and check_password_hash(usuario["password"], password):
        return True
    return False

# Flujo principal
def flujo_principal():
    while True:
        print("\nSeleccione una opción:")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            email = input("Ingrese su email: ")
            if not validar_email(email):
                print("El correo ingresado no tiene un formato válido.")
                continue
            if verificar_usuario(email):
                print(f"Usuario con email {email} ya existe.")
            else:
                password = input("Ingrese su contraseña para el registro: ")
                registrar_usuario(email, password)

        elif opcion == "2":
            email = input("Ingrese su email: ")
            if not validar_email(email):
                print("El correo ingresado no tiene un formato válido.")
                continue
            password = input("Ingrese su contraseña: ")
            if iniciar_sesion(email, password):
                print(f"Inicio de sesión exitoso para {email}.")
            else:
                print("Credenciales incorrectas o usuario no registrado.")

        elif opcion == "3":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida, por favor elija una opción correcta.")

# Ejecutar el flujo principal
flujo_principal()
