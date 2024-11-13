from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/especialistas')
def especialistas():
    # conectar esta wea a la base de datos
    especialistas_data = [
        {'nombre': 'Adalis Amanda Rodríguez', 'especialidad': 'Cirugía Plástica', 'foto': 'medico3.png'},
        {'nombre': 'Adolfo Cid Guzmán', 'especialidad': 'Medicina General', 'foto': 'medi1.jpg'},
        {'nombre': 'Luis Pérez', 'especialidad': 'Cardiología', 'foto': 'foto2.jpg'},
        {'nombre': 'María Rodríguez', 'especialidad': 'Pediatría', 'foto': 'foto3.jpg'},
        {'nombre': 'Juan Pérez', 'especialidad': 'Ginecología', 'foto': 'foto4.jpg'},
        {'nombre': 'Juan Pérez', 'especialidad': 'Ginecología', 'foto': 'foto4.jpg'},

    ]
    return render_template('especialistas.html', especialistas=especialistas_data)

if __name__ == '__main__':
    app.run(debug=True)
