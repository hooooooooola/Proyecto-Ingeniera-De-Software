from src.database.User import *
from abc import abstractmethod

class Administrador(User):
    
    def __init__(self, DatabaseConnection) -> None:
        super().__init__(DatabaseConnection)

    def create(self, data: dict) -> None:
        query = "INSERT INTO users (name, age, rut, password, rol) VALUES (%s, %s, %s, %s, 1)"
        params = (data.get('name'), data.get('age'), data.get('rut'), data.get('password'),)
        try:
            self.db.executeQuery(query, params)
        except Exception as e:
            print("Error al insertar:", e)
    
    def read(self, data: dict = None) -> list:
        # id_user: int = None, rol: int = 0 necesito eso s

        query = f"SELECT * FROM users WHERE rol = 1 AND id = %s" if data != None else f"SELECT * FROM users WHERE rol = 1"
        params = (data.get('id'),) if data != None else ()

        print(query)

        # Try para las excepciones
        try:
            self.db.executeQuery(query, params)
            results = self.db.fetchResults(query)
            return results

        except Exception as e:
            print("Error al obtener registros:", e)
            return []
        
    def get_rol(self) -> None:
        print("Administrador")