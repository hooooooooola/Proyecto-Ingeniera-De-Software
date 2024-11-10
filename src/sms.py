from hashlib import algorithms_available

import vonage
from DatabaseConnection import DatabaseConnection
from Model import Modelo
import requests
import json
from DatabaseConnection import DatabaseConnection
from Model import Modelo

def enviar_mensaje_usuariosms(rut):
    # Configuración de la base de datos
    database_config = {
        "database_name": "proyecto_software",
        "user": "postgres",
        "password": "1234",
        "host": "localhost",
        "port": "5432"
    }

    # Conectar a la base de datos
    db_connection = DatabaseConnection(**database_config)
    db_connection.connect()

    # Instancia de Modelo
    modelo = Modelo(db_connection)

    # Buscar el usuario por RUT
    usuario_encontrado = None
    usuarios = modelo.read()
    for usuario in usuarios:
        if usuario[3] == rut:
            usuario_encontrado = usuario
            break

    # Desconectar de la base de datos
    db_connection.disconnect()

    if usuario_encontrado:
        numero_destinatario = usuario_encontrado[6]  # Asumimos que el número de teléfono está en el índice 6

        # Crear cliente Vonage
        client = vonage.Client(key="181c0dff", secret="DHtIPe2Ra7dWpVKo")
        sms = vonage.Sms(client)

        # Enviar mensaje de texto
        responseData = sms.send_message(
            {
                "from": "Vonage APIs",
                "to": numero_destinatario,
                "text": "OLA\n",
            }
        )

        # Verificar respuesta
        if responseData["messages"][0]["status"] == "0":
            print("Mensaje enviado correctamente.")
        else:
            print(f"El mensaje falló con el error: {responseData['messages'][0]['error-text']}")
    else:
        print("Usuario no encontrado con el RUT especificado")


def enviar_mensaje_usuariowsp(rut):
            # Configura tu clave y secreto de la API
            API_KEY = "181c0dff"
            API_SECRET = "DHtIPe2Ra7dWpVKo"

            # Configuración de la base de datos
            database_config = {
                "database_name": "proyecto_software",
                "user": "postgres",
                "password": "1234",
                "host": "localhost",
                "port": "5432"
            }

            # Conectar a la base de datos
            db_connection = DatabaseConnection(**database_config)
            db_connection.connect()

            # Instancia de Modelo
            modelo = Modelo(db_connection)

            # Buscar el usuario por RUT
            usuario_encontrado = None
            usuarios = modelo.read()
            for usuario in usuarios:
                if usuario[3] == rut:
                    usuario_encontrado = usuario
                    break

            # Desconectar de la base de datos
            db_connection.disconnect()

            if usuario_encontrado:
                numero_destinatario = usuario_encontrado[6]  # Asumimos que el número de teléfono está en el índice 6

                # URL de la API de Vonage para mensajes
                url = "https://messages-sandbox.nexmo.com/v1/messages"

                # Encabezados de la solicitud
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                }

                # Datos de la solicitud con el número de la base de datos
                data = {
                    "from": "14157386102",
                    "to": numero_destinatario,
                    "message_type": "text",
                    "text": "OLA",
                    "channel": "whatsapp"
                }

                # Realizar la solicitud POST con autenticación
                response = requests.post(url, headers=headers, data=json.dumps(data), auth=(API_KEY, API_SECRET))

                # Imprimir la respuesta
                print(response.status_code)
                print(response.json())
            else:
                print("Usuario no encontrado con el RUT especificado")



