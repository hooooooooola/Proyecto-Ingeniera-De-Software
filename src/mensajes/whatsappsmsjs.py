import vonage
import requests
import json

# Clave y secreto de la API
API_KEY = "181c0dff"
API_SECRET = "DHtIPe2Ra7dWpVKo"

# URL de la API de Vonage para mensajes
url = "https://messages-sandbox.nexmo.com/v1/messages"

# Encabezados de la solicitud
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Datos de la solicitud
data = {
    "from": "14157386102",  # El número de Vonage de origen
    "to": "56937135522",    # Tu número de destino
    "message_type": "text",
    "text": "OLA",
    "channel": "whatsapp"
}

# Realizar la solicitud POST con autenticación
response = requests.post(url, headers=headers, data=json.dumps(data), auth=(API_KEY, API_SECRET))

if response.status_code == 202:
    print("Mensaje enviado correctamente")
else:
    print("Error al enviar el mensaje")

print(response.json())
