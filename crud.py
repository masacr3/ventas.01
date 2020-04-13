ARCHIVO = 'basedatos.txt'

def leer():
    d = {}
    with open(ARCHIVO,'r') as f:
        for linea in f:
            codigoBarra, marca, descripcion, precioMayorista, precioNegocio, fecha = linea.rstrip().split(',')
            d[codigoBarra] = [codigoBarra, marca, descripcion, precioMayorista, precioNegocio, fecha]
        
    return d

def actualizar(producto):
    
    basedatos = leer()

    if producto[0] in basedatos:
        del basedatos[producto[0]]

    basedatos[ producto[0]] = producto 

    with open(ARCHIVO,'w') as f:

        for k in basedatos:
            f.write( ','.join( basedatos[k] )+'\n' )

def eliminar(producto):

    basedatos = leer()

    if producto[0] not in basedatos: return 

    del basedatos[producto[0]]
    
    with open(ARCHIVO,'w') as f:
        for k in basedatos:
            f.write( ','.join( basedatos[k] ) +'\n' )

def estaProducto(codigoBarras):
    basedatos = leer()

    return (True, basedatos[codigoBarras]) if codigoBarras in basedatos else (False,[])