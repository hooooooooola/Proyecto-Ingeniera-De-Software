from DatabaseConnection import DatabaseConnection
from Model import Modelo
from sms import enviar_mensaje_usuariosms
from sms import enviar_mensaje_usuariowsp

def main():
    database_config = {
        "database_name": "proyecto_software",
        "user": "postgres",
        "password": "1234",
        "host": "localhost",
        "port": "5432"
    }

    # Establecer conexión
    db_connection = DatabaseConnection(**database_config)
    db_connection.connect()

    # Instancia de Modelo
    modelo = Modelo(db_connection)

    # Create (puedes comentar esto si ya tienes datos en tu tabla)
    #data = {"name": "Rodrigo", "age": 19, "rut": 12234-5, "password": "1234", "rol": 1, "numero": "56937135522"}
    #modelo.create(data)

    # Read y enviar mensaje al primer usuario en la lista
    lista = modelo.read()
    for i in lista:
        i = str(i).replace('(', '').replace(')', '').replace(',', '').replace("'", '')
        i = i.split(' ')
        print(f"Id: {i[0]} - nombre: {i[1]} - edad: {i[2]} - rut: {i[3]} - contraseña: {i[4]} - rol: {i[5]} - numero: {i[6]}")

    enviar_mensaje_usuariowsp(12229)
    enviar_mensaje_usuariosms(12229)

    # Desconectar conexión
    db_connection.disconnect()

if __name__ == "__main__":
    main()
