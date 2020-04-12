from flask import Flask, render_template, request
import crud as Crud

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('cargadatos.html')

@app.route('/cargadatos', methods = ['POST'])
def cargadatos():
    cod = request.form['cod']
    marca = request.form['marca']
    descripcion = request.form['descripcion']
    valormayorista = request.form['valormayorista']
    valornegocio = request.form['valornegocio']
    fecha = request.form['fecha']

    producto = [cod, marca, descripcion, valormayorista, valornegocio, fecha]

    Crud.actualizar(producto)
    
    return 'datos cargados exitosamente'
