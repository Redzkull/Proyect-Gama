from auth_mongo import validar_email, verificar_usuario, verificar_autenticacion
from cone_mongo import get_db
from getpass import getpass

# Función para registrar un nuevo usuario
def registrar_usuario():
    email = input("Ingrese su email: ")
    if not validar_email(email):
        print("El correo ingresado no tiene un formato válido.")
        return
    
    if verificar_usuario(email):
        print(f"Usuario con email {email} ya existe.")
        return
    
    # Solicita una contraseña segura
    password = getpass("Ingrese su contraseña: ")
    
    # Guarda el usuario en la base de datos
    db = get_db()
    db["usuarios"].insert_one({"email": email, "password": password})
    print("Usuario registrado con éxito.")

# Función para iniciar sesión
def iniciar_sesion():
    email = input("Ingrese su email: ")
    if not verificar_usuario(email):
        print("Usuario no encontrado. Por favor, regístrese.")
        return
    
    password = getpass("Ingrese su contraseña: ")
    
    # Comprobar si el correo y la contraseña coinciden
    db = get_db()
    usuario = db["usuarios"].find_one({"email": email, "password": password})
    if usuario:
        print("Inicio de sesión exitoso.")
    else:
        print("Contraseña incorrecta.")

# Menú principal
def menu():
    while True:
        print("\nSeleccione una opción:")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        
        opcion = input("Opción: ")
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
