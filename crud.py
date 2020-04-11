ARCHIVO = 'baseDatos.txt'

def escribirArchivo(datos):

    if __esta(datos):
        return 

    with open(ARCHIVO,'a') as f:
        f.write(datos+'\n')
    
    print('se han escrito los datos exitosamente')


def verBaseDatos():
    baseDatos = []
    with open(ARCHIVO,'r') as f:
        for linea in f:
            baseDatos.append( armarPaquete(linea) )
    return baseDatos


def armarPaquete(linea):
    diccionario = {}
    nombre, deuda = linea.rstrip().split(',')
    diccionario['cliente'] = { 'nombre' : nombre , 'deuda': deuda }
    return diccionario
    

def __esta(datos):
    target = datos.split(',')[0]
    with open(ARCHIVO,'r') as f:
        for linea in f:
            nombre, cantidad = linea.rstrip().split(',')
            if target == nombre :
                print('el usuario se encontraba en su base de datos')
                return True
    print('el usuario no se encontraba en la base de datos')
    return False
    