import math 
def pedirDatos():
    diametro=float(input("Dame el diametro: "))
    altura=float(input("Dame la altura: "))
    return diametro, altura
def calcVolumen(diametrof, alturaf):
    radio=diametrof/2
    volumenf=math.pi*pow(radio,2)*alturaf
    return volumenf

diametro, altura=pedirDatos()
vol=calcVolumen(diametro, altura)
print("El volumen es: ", vol)