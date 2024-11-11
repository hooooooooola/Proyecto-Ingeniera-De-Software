from database.User import *
from abc import abstractmethod

class Administrador(User):
    
    def __init__(self, DatabaseConnection) -> None:
        super().__init__(DatabaseConnection)
    
    def read(self, data: dict = None) -> list:
        # id_user: int = None, rol: int = 0 necesito eso s

        query = f"SELECT * FROM users WHERE rol = 1 AND id = %s" if data.get('id') else f"SELECT * FROM users WHERE rol = 1"
        params = (data.get('id'),) if data.get('id') else ()

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