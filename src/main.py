from psycopg2 import connect

from DatabaseConnection import DatabaseConnection
from Model import Modelo

def main():
    database_config = {
        "database_name": "proyecto_software",
        "user": "postgres",
        "password": "admin1234",
        "host": "localhost",
        "port": "5432"
    }

    # Establecer conexion
    db_connection = DatabaseConnection(**database_config)
    db_connection.connect()

    # Instancia de Modelo
    modelo = Modelo(db_connection)


    # Create
    data = {"name": "javier", "age": 20, "rut": 1234, "password": "hola", "rol": 1}
    modelo.create(data)



if __name__ == "__main__":
    main()