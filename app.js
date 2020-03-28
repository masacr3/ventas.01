const box = document.querySelector('.cb')
const ptotal = document.querySelector('.p-total')
const table = document.querySelector('.table')

let bd = ['7790072002080,celusal,sal fina 500g,55','7793940328008,la serenisima,queso rallado 40g,69']

function creaProducto(cad){
    let split = cad.split(',')
    let producto = {
        id : split[0],
        marca: split[1],
        descripcion: split[2],
        precio: parseFloat(split[3])
    }
    return producto
}

let listaP = []

bd.forEach((producto)=>{
    listaP.push(creaProducto(producto))
})

let i=0

while(i<2){
    console.log(listaP[i].marca)
    i += 1
}

box.addEventListener('keypress',(e)=>{
    if (e.keyCode == 13){
        const id = box.value 

        listaP.forEach((producto)=>{
            if ( producto.id == id){
                    const estaID = document.querySelector(`#a${id}`)
                    
                    if( estaID == null){
                        row( producto.id, producto.marca, producto.descripcion, producto.precio, 1, producto.precio)
                    }
                    else{
                        const cantidad = document.querySelector(`#a${id} .p-cantidad`)
                        const precio = parseFloat(document.querySelector(`#a${id} .p-precio`).innerHTML.split('$')[1])
                        const subtotal = document.querySelector(`#a${id} .p-subtotal`)

                        cantidad.innerHTML = parseFloat(cantidad.innerHTML) + 1
                        const nuevosub = parseFloat(subtotal.innerHTML.split('$')[1]) + precio 
                        subtotal.innerHTML = '$'+nuevosub
                    }
                    let nuevoprecio = parseFloat(ptotal.innerHTML.split('$')[1]) + producto.precio 
                        ptotal.innerHTML = "$" + nuevoprecio
                    
            }

        })

        box.value = ""
        box.focus()
    }
})

function row(id, marca, descripcion,precio,cantidad,subtotal){
    const template = `<div class="row" id="a${id}">
                        <div class="row-t">
                            <div class="col-t1">
                                <div class="t-marca">
                                    <p class="p-marca">${marca}
                                        <span class="p-cantidad">${cantidad}</span>
                                    </p>
                                </div>
                                <div class="t-descripcion">
                                    <p class="p-descripcion">${descripcion}</p>
                                </div>
                            </div>
                            <div class="col-t2">
                                <div class="t-precio">
                                    <p class="p-precio">$${precio}</p>
                                </div>
                            </div>
                            <div class="col-t3">
                                <div class="t-subtotal">
                                    <p class="p-subtotal">$${subtotal}</p>
                                </div>
                            </div>
                        </div>
                    </div>
    
    `
    const fila = document.createElement('div')
    table.appendChild(fila)

    fila.innerHTML = template
}