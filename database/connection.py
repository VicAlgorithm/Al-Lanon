from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.client = None
            cls._instance.db = None
        return cls._instance

    def connect(self):
        """Conecta a la base de datos MongoDB"""
        try:
            self.client = MongoClient('localhost', 27017, serverSelectionTimeoutMS=5000)
            # Verificar la conexión
            self.client.admin.command('ping')
            self.db = self.client['inventario_emocional']
            print("Conexión exitosa a MongoDB")
            return True
        except ConnectionFailure as e:
            print(f"Error al conectar con MongoDB: {e}")
            return False

    def get_collection(self, collection_name):
        """Obtiene una colección de la base de datos"""
        if self.db is not None:
            return self.db[collection_name]
        return None

    def close(self):
        """Cierra la conexión a la base de datos"""
        if self.client:
            self.client.close()
            print("Conexión cerrada")
