from pymongo import MongoClient

# Función para obtener la base de datos
def get_db():
    # Conexión a MongoDB (sin verificación de conexión dentro de esta función)
    client = MongoClient("mongodb+srv://Manuel:Manuel.mtz@cluster0.qjilen8.mongodb.net/?retryWrites=true&w=majority")
    
    # Selecciona y devuelve la base de datos "data_user"
    db = client["data_user"]
    
    return db
