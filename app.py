from flask import Flask, render_template, request, jsonify
import crud as Crud
from datetime import date

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('cargadatos.html')

@app.route('/ventas')
def test():
    return render_template('ventas.html')

@app.route('/verificar', methods = ['POST'])
def verificar():
    cod = request.form['cod']

    rta, referencia = Crud.estaProducto(cod)

    d ={
        'rta' : rta,
        'referencia' : referencia
    }

    return jsonify(d)


@app.route('/actualizardatos')
def actualizardatos():
    return render_template('actualizardatos.html')

@app.route('/cargadatos', methods = ['POST'])
def cargadatos():
    cod = request.form['cod']
    marca = request.form['marca']
    descripcion = request.form['descripcion']
    valormayorista = request.form['valormayorista']
    valornegocio = request.form['valornegocio']
    fecha = str(date.today())

    producto = [cod, marca, descripcion, valormayorista, valornegocio, fecha]

    Crud.actualizar(producto)
    
    return 'datos cargados exitosamente'
