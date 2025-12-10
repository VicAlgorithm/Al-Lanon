from datetime import datetime
import hashlib

class Usuario:
    """Clase base para usuarios del sistema"""

    @staticmethod
    def hash_password(password):
        """Hashea una contraseña usando SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def verify_password(password, hashed_password):
        """Verifica si una contraseña coincide con su hash"""
        return Usuario.hash_password(password) == hashed_password


class Miembro:
    """Modelo para miembros de Al-Anon"""

    @staticmethod
    def crear(collection, nombre, email, password):
        """Crea un nuevo miembro en la base de datos"""
        # Verificar si el email ya existe
        if collection.find_one({"email": email}):
            return {"success": False, "message": "El email ya está registrado"}

        miembro = {
            "nombre": nombre,
            "email": email,
            "password": Usuario.hash_password(password),
            "fecha_registro": datetime.now(),
            "registros": []
        }

        result = collection.insert_one(miembro)
        return {"success": True, "message": "Miembro registrado exitosamente", "id": str(result.inserted_id)}

    @staticmethod
    def login(collection, email, password):
        """Inicia sesión de un miembro"""
        miembro = collection.find_one({"email": email})

        if not miembro:
            return {"success": False, "message": "Email no encontrado"}

        if Usuario.verify_password(password, miembro["password"]):
            return {"success": True, "message": "Login exitoso", "usuario": {
                "id": str(miembro["_id"]),
                "nombre": miembro["nombre"],
                "email": miembro["email"]
            }}
        else:
            return {"success": False, "message": "Contraseña incorrecta"}


class Administrador:
    """Modelo para administradores del sistema"""

    @staticmethod
    def crear(collection, nombre, email, password, codigo_acceso):
        """Crea un nuevo administrador (requiere código de acceso)"""
        # Código de acceso temporal para crear administradores
        CODIGO_MAESTRO = "ALANON2024"

        if codigo_acceso != CODIGO_MAESTRO:
            return {"success": False, "message": "Código de acceso inválido"}

        # Verificar si el email ya existe
        if collection.find_one({"email": email}):
            return {"success": False, "message": "El email ya está registrado"}

        administrador = {
            "nombre": nombre,
            "email": email,
            "password": Usuario.hash_password(password),
            "fecha_registro": datetime.now(),
            "tipo": "administrador"
        }

        result = collection.insert_one(administrador)
        return {"success": True, "message": "Administrador registrado exitosamente", "id": str(result.inserted_id)}

    @staticmethod
    def login(collection, email, password):
        """Inicia sesión de un administrador"""
        admin = collection.find_one({"email": email})

        if not admin:
            return {"success": False, "message": "Email no encontrado"}

        if Usuario.verify_password(password, admin["password"]):
            return {"success": True, "message": "Login exitoso", "usuario": {
                "id": str(admin["_id"]),
                "nombre": admin["nombre"],
                "email": admin["email"]
            }}
        else:
            return {"success": False, "message": "Contraseña incorrecta"}
