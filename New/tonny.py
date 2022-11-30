cadena= "Te quiero solo como amigo"
print("Cadena invertida")
cadenainvertida=""

print(cadena[0 : 2])
print(cadena[-3 : ])
print(cadena[: : 2])
print(cadena[: : -1])
print(cadena + cadena[: : -1])

#########################################33333
#Crear un programa que tenga una variable con la cadena “Separado” y un carácter de coma (,); e inserte el carácter entre cada letra de la cadena. Ej: separar y , debería devolver s,e,p,a,r,a,r

#Pista: Debes utilizar un método de las cadenas llamado “Replace”, recuerda que la posición de los caracteres empieza en 0.
stringc="separado"
for i in range(0,1,1):
    print(stringc[i])