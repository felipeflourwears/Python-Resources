#Realizar un algoritmo que calcule el factorial de un número dado.
def pedirDatos():
    num=float(input("Dame un numero para factorial: "))
    return num

def calcFactorial(fact):
    if(fact<0):
        print("No existe factorial menor a 0")
    elif(fact==0):
        print("El factorial de 0 es 1")
    else:
        contfact=1
        while(fact>1):
            contfact=contfact*fact
            fact=fact-1
    return contfact

num=pedirDatos()
factorial=calcFactorial(num)
print("Factorial de ", num, "es: ", factorial)

        