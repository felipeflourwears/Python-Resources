def pedirDatos():
    catetoOpuesto=float(input("Dame el cateto Opuesto: "))
    catetoAdyacente=float(input("Dame el cateto Adyacente: "))
    return catetoOpuesto, catetoAdyacente

def hipotenusa(catetoOpuesto, catetoAdyacente):
    hipotenusaf=pow(pow(catetoOpuesto,2)+pow(catetoAdyacente,2),0.5)
    return hipotenusaf
def area(catetoOpuesto, catetoAdyacente):
    areaf=(catetoOpuesto*catetoAdyacente)/2
    return areaf

catetoOp, catetoAd=pedirDatos()
h=hipotenusa(catetoOp, catetoAd)
a=area(catetoOp,catetoAd)
print("El valor de la hipotenusa es: ", h)
print("El valor del area del triangulo es: ", a)
