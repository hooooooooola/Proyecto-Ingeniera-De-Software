from src.database.User import User
from abc import abstractmethod

class Paciente(User):
    
    def __init__(self, DatabaseConnection) -> None:
        super().__init__(DatabaseConnection)

    def create(self, data: dict) -> None:
        query = "INSERT INTO users (name, mail, number, age, rut, rol) VALUES (%s, %s, %s, %s, %s, 3)"
        params = (data.get('name'), data.get('mail'), data.get('number'), data.get('age'), data.get('rut'),)
        try:
            self.db.executeQuery(query, params)
        except Exception as e:
            print("Error al insertar:", e)
    
    def read(self, data: dict = None) -> list:
        # id_user: int = None, rol: int = 0 necesito eso s

        query = "SELECT * FROM users WHERE rol = 3 AND id=%s" if data else "SELECT * FROM users WHERE rol = 3"
        params = (data.get("id"),) if data else ()  # (data.get("id"),) if data else ()

        # Try para las excepciones
        try:
            self.db.executeQuery(query, params)
            results = self.db.fetchResults(query, params)
            return results

        except Exception as e:
            print("Error al obtener registros:", e)
            return []

        except Exception as e:
            print("Error al obtener registros:", e)
            return []

    def get_rol(self) -> None:
        print("Paciente")