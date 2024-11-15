from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')
@app.route('/administrador')
def administrador():
    return render_template('administrador.html')


@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Respuesta recibida:", data)  #Imprime la respuesta

    try:

        user_response = data.get("text", "").strip().lower()
        print(f"Respuesta del usuario: {user_response}")

        if user_response in ["sí", "si"]:
            print("Usuario ha confirmado la cita.")
            # Lógica
        elif user_response == "no":
            print("Usuario ha cancelado la cita.")
            # Lógica
        else:
            print("Respuesta desconocida.")

    except Exception as e:
        print(f"Error al procesar la respuesta: {e}")

    return jsonify({"status": "success"}), 200




if __name__ == '__main__':
    app.run(debug=True, port=8080)