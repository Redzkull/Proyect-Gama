from pymongo import MongoClient, errors

try:
    # URI de conexión con SSL habilitado
    uri = "mongodb+srv://Manuel:Manuel.mtz@cluster0.qjilen8.mongodb.net/?retryWrites=true&w=majority&tls=true"
    client = MongoClient(uri)  # Conexión a MongoDB Atlas
    db = client.test  # Conexión de prueba a una base de datos
    
    print("Conexión exitosa a MongoDB Atlas")
    
    usuario = {
        "email": "prueba1@asdasd.com",
        "token": "1234567890"  # Token de prueba
    }
    db["usuarios"].insert_one(usuario)
    print("Usuario de prueba insertado.")
except errors.ServerSelectionTimeoutError as err:
    print("Error de conexión:", err)



