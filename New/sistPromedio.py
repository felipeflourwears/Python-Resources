p1=float(input("Dame el promedio de la Practica 1: "))
p2=float(input("Dame el promedio de la Practica 2: "))
p3=float(input("Dame el promedio de la Practica 3: "))
ep=p1=float(input("Dame el promedio del Examen Parcial: "))
ef=float(input("Dame el promedio del Examen Final: "))

#PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6
pp=(p1+p2+p3)/3
promediofinal=(pp+2*ep+3*ef)/6
print("El promedio del alumno es de: ", promediofinal)