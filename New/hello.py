print("Hello world iniciation")
print("Resultado es: ",pow((3+2)/(2*5),2))
print("Resultado es: ",((3+2)/(2*5))**2)

##Ejerccio2
#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete, así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Un cliente frecuente pide la cantidad de 23 payasos y 54 muñecas, realiza un programa que muestre el peso total de toda la venta.

#Pista: Suponiendo que un cliente pide 5 payasos y 3 muñecas, la juguetería debería hacer la multiplicación de la cantidad de payasos con su peso, al igual que las muñecas; al tener ambos totales de peso, se debe sumar.

#23 Payasos --> 112 g
#54 Munecas --> 75g

# numpayasos= int(input("Dame el numero de payasos: "))
# nummuñecas=int(input("Dame el numero de muñecas: "))
# PesoP=112*numpayasos
# PesoM=75*nummuñecas
# Pesototal=(PesoM*PesoP)
# kilos=Pesototal/1000
# print(Pesototal, "gramos")
# print(kilos, "kg")


#Crear un programa, que tenga una variable con la cadena “Te quiero solo como amigo”, y muestre la siguiente información:

#• Imprima los dos primeros caracteres.

#• Imprima los tres últimos caracteres.

#• Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena fuera “recta” debería imprimir rca

#• Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh

#• Imprima la cadena en un sentido y en sentido inverso. Ej: Si la cadena es “reflejo” imprime reflejoojelfer.

cadena= "Te quiero solo como amigo"
print(cadena)
print(type(cadena))
print("Cantidad de cadena:", len(cadena))
print(cadena[0:2])
print(cadena[22:25])
cadenanew=[]
print("Cada dos caracteres")
for i in range(0,len(cadena), 2):
    cadenanew.append(cadena[i])
    print(cadena[i], end=" ")

print(" ")
print("Cadena al reves")

def invertir_cadena(cadena):
    return cadena[::-1]


print("Cadena invertida")
cadenainvertida=""

for letra in cadena:
    cadenainvertida=letra+cadenainvertida
print(cadenainvertida)
print("passInvertido")

cadenaCorrecta=""
for letra in cadena:
    cadenaCorrecta=cadenaCorrecta+letra
print(cadenaCorrecta)
print("passCorrecto")

print("Video")
print(cadena[0 : 2])
print(cadena[-3 : ])
print(cadena[: : 2])
print(cadena[: : -1])
print(cadena + cadena[: : -1])