from src.database.User import *
from abc import abstractmethod

class Medico(User):
    
    def __init__(self, DatabaseConnection) -> None:
        super().__init__(DatabaseConnection)
    
    def create(self, data: dict) -> None:
        query = "INSERT INTO users (name, age, rut, password, rol) VALUES (%s, %s, %s, %s, 2)"
        params = (data.get('name'), data.get('age'), data.get('rut'), data.get('password'),)
        try:
            self.db.executeQuery(query, params)
        except Exception as e:
            print("Error al insertar:", e)
    
    def read(self, data: dict = None) -> list:
        # id_user: int = None, rol: int = 0 necesito eso s

        query = "SELECT * FROM users WHERE rol = 2 AND id=%s" if data else "SELECT * FROM users WHERE rol = 2"
        params = (data.get("id"),) if data else () # (data.get("id"),) if data else ()

        print(query)

        # Try para las excepciones
        try:
            self.db.executeQuery(query, params)
            results = self.db.fetchResults(query, params)
            return results

        except Exception as e:
            print("Error al obtener registros:", e)
            return []
        
    def get_rol(self) -> None:
        print("Medico")

    def read_description(self) -> list:
        query = "SELECT u.name, im.especialidad, im.foto, im.descripcion FROM users u JOIN info_medico im ON u.id = im.id"
        params = ()

        try:
            self.db.executeQuery(query, params)
            results = self.db.fetchResults(query, params)
            return results
        except Exception as e:
            print("Error al obtener registros:", e)
            return []