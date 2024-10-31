import string

import psycopg2

class DatabaseConnection:
    # Variables
    database_name: str
    user: str
    password: str
    host: str
    port: int

    # Inicializar conexion
    def __init__(self, database_name: str = None, user: str = None,
                 password: str = None, host: str = None, port: int = None):
        self.database_name = database_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None

    def connect(self) -> None:
        try:
            self.connection = psycopg2.connect(
                dbname = self.database_name,
                user = self.user,
                password = self.password,
                host = self.host,
                port = self.port
            )
            print("Conexion exitosa")
        except psycopg2.Error:
            print(f"Error al conectar con la base de datos {psycopg2.Error}")

    def disconnect(self) -> None:
        if self.connection:
            self.connection.close()
            print("Conexión cerrada.")

    def executeQuery(self, query: str, params: tuple = None) -> None:
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            self.connection.commit()

    def fetchResults(self, query: str, params: tuple = None) -> list:
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()