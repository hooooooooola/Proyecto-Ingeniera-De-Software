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
    data = {"name": "chao", "age": 90, "rut": 12234, "password": "hola", "rol": 1}
    modelo.create(data)

    # Read
    lista = modelo.read()
    for i in lista:
        i = str(i).replace('(', '').replace(')', '').replace(',', '').replace("'", '')
        i = i.split(' ')
        print(f"Id: {i[0]} - nombre: {i[1]} - edad: {i[2]} - rut: {i[3]} - contraseña: {i[4]} - rol: {i[5]}")


    # Desconectar conexion
    db_connection.disconnect()

if __name__ == "__main__":
    main()