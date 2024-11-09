import requests
import json

# Configura tu clave y secreto de la API
api_key = '181c0dff'
api_secret = 'DHtIPe2Ra7dWpVKo'

# URL de la API de Mensajes de Vonage
url = "https://messages-sandbox.nexmo.com/v1/messages"

# Encabezados de la solicitud
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Datos del mensaje a enviar
data = {
    "from": "17841449184623529",  # El remitente de la cuenta de Instagram
    "to": "860918449362940",      # El ID del destinatario
    "message_type": "text",
    "text": "Ola",
    "channel": "instagram"
}

# Realiza la solicitud POST a la API
response = requests.post(url, headers=headers, data=json.dumps(data), auth=(api_key, api_secret))

# Imprime el código de estado y la respuesta de la API
print(response.status_code)
print(response.json())
