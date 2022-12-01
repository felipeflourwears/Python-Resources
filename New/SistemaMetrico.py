# // ConversionSistemametrico.cpp : Este archivo contiene la función "main". La ejecución del programa comienza y termina ahí.
# //Dados los valores de tres unidades de longitud del sistema inglés 
# //(pulgadas, yardas, pies), realice las conversiones al sistema métrico decimal (centímetros), 
# //de las tres unidades solicitadas.
yarda=float(input("Dame la cantidad de yardas: "))
pulgadas=float(input("Dame la cantidad de pulgadas: "))
pies=float(input("Dame la cantidad de pies: "))

#Sistema de valores en cm
yard = 91.44
pulgada = 2.54
pie = 30.48

myard=yarda*yard
mpulg=pulgada*pulgadas
mpies=pies*pie
print("La cantidad de pies en cm es: ", mpies)
print("La cantidad de pulgadas en cm es: ", mpulg)
print("La cantidad de yardas en cm es: ", myard)