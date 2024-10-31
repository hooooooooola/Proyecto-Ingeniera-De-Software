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

    def read(self, id_user: int = None) -> None:
        if id_user is not None:
            query = "SELECT * FROM users WHERE id = %s"
            params = (id_user,)
        else:
            query = "SELECT * FROM users"
            params = ()

        try:
            results = self.db.executeQuery(query, params)
            for valores in results:
                print(valores)

        except Exception as e:
            print("Error al obtener registros:", e)


    def update(self, data) -> None:
        pass

    def delete(self, data) -> None:
        pass

