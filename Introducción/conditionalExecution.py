#Determinar el número mayor
x=input("Introduce el primer numero: ")
y=input("Introduce el segundo numero: ")

if (x>y):
    print("El primer numero es más grande")
if(y>x):
    print("El segundo numero es mas grande")
if(x==y):
    print("Los dos numeros son iguales")

#else/elif/if
x1=input("Introduce el primer numero: ")
y2=input("Introduce el segundo numero: ")

if (x>y):
    print("El primer numero es más grande")
elif(y>x):
    print("El segundo numero es mas grande")
if(x==y):
    print("Los dos numeros son iguales")
else:
    print("Entradas inválidas")