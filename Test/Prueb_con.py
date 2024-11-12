import bcrypt
from pymongo import MongoClient

# Conexión a MongoDB (reemplaza con tus credenciales)
uri = "mongodb+srv://Manuel:Manuel.mtz@cluster0.qjilen8.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

# Seleccionar base de datos y colección
db = client["mi_base_de_datos"]
usuarios = db["usuarios"]

# Función para encriptar la contraseña
def encriptar_contraseña(password):
    salt = bcrypt.gensalt()  # Genera una sal
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)  # Encripta la contraseña
    return hashed

# Función para verificar la contraseña
def verificar_contraseña(contraseña_original, contraseña_encriptada):
    return bcrypt.checkpw(contraseña_original.encode('utf-8'), contraseña_encriptada)

# Función para insertar un nuevo usuario
def insertar_usuario(email, password, role):
    hashed_password = encriptar_contraseña(password)  # Encriptar la contraseña antes de guardarla
    usuario = {
        "email": email,
        "password": hashed_password,
        "role": role
    }
    result = usuarios.insert_one(usuario)
    return result.inserted_id

# Función para obtener un usuario por su email
def obtener_usuario_por_email(email):
    return usuarios.find_one({"email": email})

# Probar la inserción de un usuario y luego verificar la contraseña
def probar_mongo():
    # Insertar un usuario
    email = "usuario@example.com"
    password = "contraseña123"
    role = "parent"
    
    # Inserta el usuario
    user_id = insertar_usuario(email, password, role)
    print(f"Usuario insertado con ID: {user_id}")
    
    # Obtener el usuario de la base de datos
    usuario = obtener_usuario_por_email(email)
    if usuario:
        print("Usuario encontrado:")
        print(f"Email: {usuario['email']}")
        print(f"Role: {usuario['role']}")
        
        # Verificar la contraseña
        if verificar_contraseña(password, usuario['password']):
            print("Contraseña verificada correctamente")
        else:
            print("La contraseña es incorrecta")
    else:
        print("Usuario no encontrado")

# Ejecutar la prueba
probar_mongo()
