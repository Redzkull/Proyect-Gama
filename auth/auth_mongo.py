from cone_mongo import get_db

# Verificar si el usuario existe por email
def verificar_usuario(email):
    db = get_db()  # Conexión a la base de datos
    usuario = db["usuarios"].find_one({"email": email})  # Buscar al usuario por email
    
    return usuario is not None  # Devuelve True si el usuario existe, False si no

# Verificar si el token existe en la base de datos
def verificar_autenticacion(token):
    db = get_db()  # Conexión a la base de datos
    usuario = db["usuarios"].find_one({"token": token})  # Buscar al usuario por token
    
    return usuario is not None  # Devuelve True si el token existe, False si no

# Flujo de comprobación
def flujo_comprobacion():
    email = input("Ingrese su email: ")
    if verificar_usuario(email):
        print(f"Usuario con email {email} ya existe.")
    else:
        print(f"Usuario con email {email} no existe.")
        
    token = input("Ingrese su token: ")
    if verificar_autenticacion(token):
        print(f"El usuario con token {token} ya está registrado.")
    else:
        print(f"El usuario con token {token} no está registrado.")

# Ejecutar el flujo de comprobación
flujo_comprobacion()
