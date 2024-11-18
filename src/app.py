from flask import Flask, flash, redirect, render_template, request, jsonify, url_for


from src.database.DatabaseConnection import DatabaseConnection
from src.database.Medicos import Medico

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
        "rut": request.form.get('rut'),
        "nombre": request.form.get('nombre'),
        "telefono": request.form.get('telefono'),
        "edad": request.form.get('edad')
    }
    print(data) # Imprimir en consola pa cachar :D


@app.route('/servicios')
def servicios():
    return render_template('servicios.html')
@app.route('/administrador')
def administrador():
    return render_template('administrador.html')

    return redirect(url_for('especialistas'))
    
if __name__ == '__main__':
    app.run(debug=True)