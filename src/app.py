from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/especialistas')
def especialistas():
    # conectar esta wea a la base de datos
    especialistas_data = [
        {'nombre': 'Adalis Amanda Rodríguez', 'especialidad': 'Cirugía Plástica', 'foto': 'medico3.png', 'descripcion': 'Especialista en cirugía plástica y reconstructiva, con más de 10 años de experiencia en el área. Ha realizado más de 1000 cirugías plásticas y reconstructivas, con resultados exitosos en todos los casos.'},
        {'nombre': 'Adolfo Cid Guzmán', 'especialidad': 'Medicina General', 'foto': 'medi1.jpg', 'descripcion': 'Médico general con más de 5 años de experiencia en el área. Ha trabajado en diversos hospitales y clínicas de la ciudad, atendiendo a pacientes con diversas patologías.'},
        {'nombre': 'Luis Pérez', 'especialidad': 'Cardiología', 'foto': 'foto2.jpg', 'descripcion': 'Especialista en cardiología, con más de 15 años de experiencia en el área. Ha realizado más de 5000 procedimientos cardiológicos, con resultados exitosos en todos los casos.'},
        {'nombre': 'María Rodríguez', 'especialidad': 'Pediatría', 'foto': 'foto3.jpg', 'descripcion': 'Especialista en pediatría, con más de 10 años de experiencia en el área. Ha atendido a más de 1000 niños con diversas patologías, con resultados exitosos en todos los casos.'},
        {'nombre': 'Juan Pérez', 'especialidad': 'Ginecología', 'foto': 'foto4.jpg', 'descripcion': 'Especialista en ginecología, con más de 10 años de experiencia en el área. Ha atendido a más de 1000 mujeres con diversas patologías ginecológicas, con resultados exitosos en todos los casos.'},
        {'nombre': 'Juan Pérez', 'especialidad': 'Ginecología', 'foto': 'foto4.jpg', 'descripcion': 'Especialista en ginecología, con más de 13 años de experiencia en el área. Ha atendido a más de 1000 mujeres con diversas patologías ginecológicas, con resultados exitosos en todos los casos.'},

    ]
    return render_template('especialistas.html', especialistas=especialistas_data)

if __name__ == '__main__':
    app.run(debug=True)
