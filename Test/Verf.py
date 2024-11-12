import bcrypt
from pymongo import MongoClient

# Conectar con MongoDB (reemplaza con tu URI y credenciales)
uri = "mongodb+srv://Manuel:Manuel.mtz@cluster0.qjilen8.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

# Selecciona la base de datos y la colección donde almacenarás los usuarios
db = client["data_user"]
usuarios = db["usuarios"]

# Función para encriptar la contraseña
def encriptar_contraseña(password):
    salt = bcrypt.gensalt()  # Genera un "salt" para la encriptación
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)  # Encripta la contraseña
    return hashed

# Función para verificar si el email ya está registrado
def verificar_email(email):
    usuario = usuarios.find_one({"email": email})
    return usuario is not None  # Retorna True si el email ya existe

# Función para registrar un nuevo usuario
def registrar_usuario(email, password, role):
    # Verificar si el email ya está registrado
    if verificar_email(email):
        print("Error: Este correo ya está registrado.")
        return
    
    # Encriptar la contraseña antes de guardarla
    hashed_password = encriptar_contraseña(password)
    
    # Crear el diccionario con la información del nuevo usuario
    nuevo_usuario = {
        "email": email,
        "password": hashed_password,
        "role": role
    }
    
    # Insertar el nuevo usuario en la base de datos
    usuarios.insert_one(nuevo_usuario)
    print(f"Usuario {email} registrado exitosamente.")

# Ejemplo de uso: ingresar los datos del usuario
email = input("Ingrese su correo electrónico: ")
password = input("Ingrese su contraseña: ")
role = input("Ingrese su rol (padre/niño): ")

# Llamamos a la función de registro con los datos ingresados
registrar_usuario(email, password, role)
