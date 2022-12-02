

def pedirDatos():
    precio=float(input("Dame el precio del producto: "))
    descuento=float(input("Dame el descuento: "))
    return precio, descuento
    
def descuentop(precio, descuento):
    preciofinal=precio-(precio/100)*descuento
    print("El precio con descuento es: ", preciofinal)

precio, descuento=pedirDatos()
descuentop(precio, descuento)