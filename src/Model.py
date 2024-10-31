from DatabaseConnection import DatabaseConnection

class Modelo:
    def __init__(self, DatabaseConnection):
        self.db = DatabaseConnection

    def create(self, data: dict) -> None:
        query = "INSERT INTO users (name, age, rut, password, rol) VALUES (%s, %s, %s, %s, %s)"
        params = (data.get('name'), data.get('age'), data.get('rut'), data.get('password'), data.get('rol'))
        try:
            self.db.executeQuery(query, params)
        except Exception as e:
            print("Error al insertar:", e)

    def read(self, id_user: int = None) -> list:
        if id_user is not None:
            query = "SELECT * FROM users WHERE id = %s"
            params = (id_user,)
        else:
            query = "SELECT * FROM users"
            params = ()

        print(query)

        # Try para las excepciones
        try:
            self.db.executeQuery(query, params)
            results = self.db.fetchResults(query)
            return results

        except Exception as e:
            print("Error al obtener registros:", e)
            return []


    def update(self, data) -> None:
        query = "UPDATE users SET name = %s WHERE id = %s"
        params = (data.get('name'), data.get('id'))
        try:
            self.db.executeQuery(query, params)
            print("Update exitoso")
        except Exception as e:
            print("Error al actualizar registros:", e)

    def delete(self, data) -> None:
        query = "DELETE FROM users WHERE id = %s"
        params = (data.get('id'),)
        try:
            self.db.executeQuery(query, params)
            print("Delete exitoso")
        except Exception as e:
            print("Error al eliminar registros:", e)

    def limpiarDatabase(self):
        query = "TRUNCATE TABLE users"
        self.db.executeQuery(query)

