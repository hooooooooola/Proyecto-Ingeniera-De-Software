import vonage
import requests
import json
import subprocess

# Claves de API para Vonage
API_KEY = "181c0dff"
API_SECRET = "DHtIPe2Ra7dWpVKo"

def enviar_mensaje_usuariosms(numero):
    # Crear cliente Vonage
    client = vonage.Client(key=API_KEY, secret=API_SECRET)
    sms = vonage.Sms(client)

    # Enviar mensaje de texto
    responseData = sms.send_message(
        {
            "from": "Vonage APIs",
            "to": numero,
            "text":(
            "Hola.\nTe recordamos que tienes una cita médica programada el dia XX XX/XX/XXXX.\n"
            "Médico Asignado: Dr. Nombre Apellido1\n"
            "Especialidad: XXXXXXXologo\n"
            "Lugar: Clinica TAL TAL\n"
            "Hora: XX:XX\n"
            "-Para confirmar su asistencia puede ingresar al siguiente link\n"
            "-Alternativamente puede llamar al siguiente numero\n"
            " +56937135522 \n\n"
            ),
        }
    )

    # Verificar respuesta
    if responseData["messages"][0]["status"] == "0":
        print("Mensaje SMS enviado correctamente.")
    else:
        print(f"El mensaje SMS falló con el error: {responseData['messages'][0]['error-text']}")

def enviar_mensaje_usuariowsp(numero):
    # URL de la API de Vonage para mensajes en el sandbox
    url = "https://messages-sandbox.nexmo.com/v1/messages"

    # Encabezados de la solicitud
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    # Datos de la solicitud con el número en formato internacional
    data = {
        "from": "14157386102",
        "to": numero,
        "message_type": "text",
        "text": (
            "*Hola*.\nTe recordamos que tienes una cita médica programada para el día XX XX/XX/XXXX.\n"
            "*Médico Asignado:* Dr. Nombre Apellido1\n"
            "*Especialidad:* XXXXXXXologo\n"
            "*Lugar:* Clinica TAL TAL\n"
            "*Hora: XX:XX*\n"
            "*¿Confirmas tú asistencia?*\n\n"
            "Responde con *'Sí'* para confirmar o *'No'* para cancelar."
        ),
        "channel": "whatsapp"
    }

    # Realizar la solicitud POST con autenticación
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data), auth=(API_KEY, API_SECRET))

        # Imprimir la respuesta completa para diagnóstico
        if response.status_code == 202:
            print("Mensaje de WhatsApp enviado correctamente.")
        else:
            print("Error al enviar mensaje de WhatsApp:")
            print("Código de estado:", response.status_code)
            print("Respuesta completa de la API:", response.json())
    except Exception as e:
        print("Error al realizar la solicitud:", str(e))

#    def enviar_mensaje_con_curl(numero):
#        # Replicando el comando `curl` desde Python
#        curl_command = [
#            "curl",
#            "-X", "POST",
#            "https://messages-sandbox.nexmo.com/v1/messages",
#            "-u", f"{API_KEY}:{API_SECRET}",
#            "-H", "Content-Type: application/json",
#            "-H", "Accept: application/json",
#            "-d", json.dumps({
#                "from": "14157386102",
#                "to": numero,
#                "message_type": "text",
#                "text": "Hola desde Python (curl)",
#                "channel": "whatsapp"
#            })
#        ]

#        try:
#            result = subprocess.run(curl_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#            print("Salida de `curl`:", result.stdout)
#            print("Errores de `curl`:", result.stderr)
#        except Exception as e:
#            print("Error al ejecutar `curl` desde Python:", str(e))






# Ejemplo de uso
#enviar_mensaje_usuariowsp("56937135522")
#enviar_mensaje_con_curl("56937135522")
enviar_mensaje_usuariosms("56937135522")
