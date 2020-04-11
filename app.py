from flask import Flask, render_template, request
import crud as Crud

app = Flask(__name__)

@app.route('/')
def index():
    titulo = 'Carga de datos'

    return render_template('index.html', titulo=titulo)

@app.route('/producto', methods = ['POST'])
def producto():
    producto = request.form['cliente']
    cantidad = request.form['precio']

    cadena = '{},{}'.format(producto,cantidad)

    Crud.escribirArchivo(cadena)

    listaUsuarios = Crud.verBaseDatos()
    
    return render_template('clientes.html', listaUsuarios = listaUsuarios)
    
