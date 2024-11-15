from psycopg2 import connect

from src.database.DatabaseConnection import DatabaseConnection
from src.database.Pacientes import Paciente
from src.database.Medicos import Medico
from src.database.Administrador import Administrador
from src.sms import *


def main():
    database_config = {
        "database_name": "proyecto_software",
        "user": "postgres",
        "password": "1234",
        "host": "localhost",
        "port": "5432",
    }

    # Establecer conexion
    db_connection = DatabaseConnection(**database_config)
    db_connection.connect()

    # Instancia de Modelo
    modelo = Paciente(db_connection)

    # Read
    dicc = {"id": 51}
    lista = modelo.read(dicc)
    for i in lista:
        i = str(i).replace('(', '').replace(')', '').replace(',', '').replace("'", '')
        i = i.split(' ')
        print(f"Id: {i[0]} - nombre: {i[1]} - edad: {i[2]} - rut: {i[3]} - contraseña: {i[4]} - rol: {i[5]}")
    
    # Read
    modelo = Administrador(db_connection)

    dicc = {"id": 47}
    lista = modelo.read(dicc)
    for i in lista:
        i = str(i).replace('(', '').replace(')', '').replace(',', '').replace("'", '')
        i = i.split(' ')
        print(f"Id: {i[0]} - nombre: {i[1]} - edad: {i[2]} - rut: {i[3]} - contraseña: {i[4]} - rol: {i[5]}")


    modelo = Medico(db_connection)

    dicc = {"id": 50}
    lista = modelo.read(dicc)
    for i in lista:
        i = str(i).replace('(', '').replace(')', '').replace(',', '').replace("'", '')
        i = i.split(' ')
        print(f"Id: {i[0]} - nombre: {i[1]} - edad: {i[2]} - rut: {i[3]} - contraseña: {i[4]} - rol: {i[5]}")

    # Desconectar conexion
    db_connection.disconnect()

if __name__ == "__main__":
    main()