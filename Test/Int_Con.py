from pymongo import MongoClient
import json

# Función para obtener la base de datos
def get_db():
    # Reemplaza con la URL de tu clúster MongoDB y tus credenciales
    client = MongoClient("mongodb+srv://Manuel:Manuel.mtz@cluster0.qjilen8.mongodb.net/test")
    db = client["data_user"]  # El nombre de la base de datos
    return db

# Simula la función de autenticación con Google que genera un token
def obtener_token_google():
    # Simulando un token generado por Google (esto es solo un ejemplo)
    # En la realidad, usarías la API de Google para obtener el token
    return "token_generado_por_google_123456789"

# Función para insertar un nuevo usuario con un token en la base de datos
def insertar_usuario_con_token(email, password, role):
    # Obtener el token de Google
    token = obtener_token_google()

    # Obtener la base de datos y la colección de usuarios
    db = get_db()
    usuarios = db["usuarios"]  # Nombre de la colección

    # Crear el documento del nuevo usuario
    nuevo_usuario = {
        "email": email,
        "password": password,  # La contraseña podría estar encriptada
        "role": role,  # El rol del usuario (por ejemplo, 'parent' o 'child')
        "token": token  # Guardar el token generado
    }

    # Insertar el documento en la colección
    usuarios.insert_one(nuevo_usuario)
    print(f"Usuario {email} insertado con éxito y token guardado.")

# Solicitar datos al usuario para crear el nuevo usuario
email = input("Ingresa el correo del usuario: ")
password = input("Ingresa la contraseña del usuario: ")
role = input("Ingresa el rol del usuario ('parent' o 'child'): ")

# Llamar a la función para insertar el usuario con el token
insertar_usuario_con_token(email, password, role)
