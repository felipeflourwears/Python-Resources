def pedirDatos():
    calf=float(input("Dame tu calificacion: "))
    return calf

def calcCalf(calificacion):
    if (calificacion==100):
        print("Excelente (:")
    elif (calificacion>=85 and calificacion<=99):
        print("Muy bien (:")
    elif(calificacion>=75 and calificacion<85):
        print("Bien (:")
    elif(calificacion>=65 and calificacion<75):
        print("Regular")
    elif(calificacion>=55 and calificacion<65):
        print("Mal")
    elif(calificacion>=0 and calificacion<55):
        print("Muy mal")
    else:
        print("Intentar nuevamente")

calf=pedirDatos()
calcCalf(calf) 