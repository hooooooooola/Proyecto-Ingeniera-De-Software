from flask import Flask, render_template

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

if __name__ == '__main__':
    app.run(debug=True)
