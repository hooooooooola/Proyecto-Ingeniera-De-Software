import vonage

client = vonage.Client(key="181c0dff", secret="DHtIPe2Ra7dWpVKo")
sms = vonage.Sms(client)
responseData = sms.send_message(
    {
        "from": "Vonage APIs",
        "to": "56937135522",
            "text": "OLA\n",
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Mensaje enviado correctamente.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")