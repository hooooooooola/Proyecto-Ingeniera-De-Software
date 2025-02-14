from flask import Flask, flash, redirect, render_template, request, jsonify, url_for
from sms import SMS

from src.database.Administrador import Administrador
from src.database.DatabaseConnection import DatabaseConnection
from src.database.Medicos import Medico
from src.database.Pacientes import Paciente

database_config = {
    "database_name": "proyecto_software",
    "user": "postgres",
    "password": "admin1234",
    "host": "localhost",
    "port": "5432",
}


app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'  # Necesario para usar flash()

# Lista global para almacenar las reservas
reservas = []

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/especialistas')
def especialistas():

    especialistas_data = []

    # Conexion base de datos
    database = DatabaseConnection(**database_config)
    database.connect()

    modelo = Medico(database)

    # lista con los valores
    lista = modelo.read_description()

    for i in lista:
        a = {'nombre': f'{i[0]}', 'especialidad': f'{i[1]}', 'foto': f'{i[2]}', 'descripcion': f'{i[3]}'}
        especialistas_data.append(a)

    database.disconnect()

    return render_template('especialistas.html', especialistas=especialistas_data)

@app.route('/reservar_hora', methods=['POST'])
def reservar_hora():
    data = {
        "rut": int(request.form.get('rut')),
        "mail": request.form.get('mail'),
        "name": request.form.get('nombre'),
        "number": int(request.form.get('number')),
        "age": int(request.form.get('edad'))
    }

    # Conexion base de datos
    database = DatabaseConnection(**database_config)
    database.connect()

    modelo = Paciente(database)
    modelo.create(data)


    data_sms = {"especialidad": "urologo", "medico": "Eduardo Parra", "fecha": "10-10-2024", "hora": "12:15-13:15"}
    mensaje_sms = SMS()
    mensaje_sms.enviar_mensaje_usuariowsp(str(request.form.get('number')), data_sms)

    database.disconnect()

    print(data) # Imprimir en consola pa cachar :D
    return render_template('inicio.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        diccionario = {'rut': request.form['rut'], 'password': request.form['password']}

        database = DatabaseConnection(**database_config)
        database.connect()

        modelo = Administrador(database)
        lista = modelo.read(diccionario)

        database.disconnect()

        if lista:  # Ejemplo de credenciales válidas
            return redirect(url_for('administrador'))
        else:
            flash("Credenciales inválidas", "error")
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/info')
def info():
    return render_template('info.html')


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
    app.run(debug=True)


