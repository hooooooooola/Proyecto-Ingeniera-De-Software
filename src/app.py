from flask import Flask, render_template

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

if __name__ == '__main__':
    app.run(debug=True)
