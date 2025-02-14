from src.database.DatabaseConnection import DatabaseConnection
from abc import ABC, abstractmethod

class User:


    def __init__(self, DatabaseConnection) -> None:
        self.db = DatabaseConnection

    @abstractmethod
    def create(self, data: dict) -> list:
        pass
    
    @abstractmethod
    def read(self, data: dict = None) -> list:
        pass

    @abstractmethod
    def get_rol(self):
        pass

    def update(self, data: dict) -> None:
        query = "UPDATE users SET name = %s WHERE id = %s"
        params = (data.get('name'), data.get('id'))
        try:
            self.db.executeQuery(query, params)
            print("Update exitoso")
        except Exception as e:
            print("Error al actualizar registros:", e)

    def delete(self, id_user: int) -> None:
        query = "DELETE FROM users WHERE id = %s"
        params = (id_user,)
        try:
            self.db.executeQuery(query, params)
            print("Delete exitoso")
        except Exception as e:
            print("Error al eliminar registros:", e)

    def limpiarDatabase(self):
        query = "TRUNCATE TABLE users"
        self.db.executeQuery(query)


