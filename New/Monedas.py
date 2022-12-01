from math import floor
def conv(monedas):
    mon10=monedas/10
    mon10=floor(mon10)
    res10=10*mon10
    monedas=monedas-res10
    mon5=monedas/5
    mon5=floor(mon5)
    res5=5*mon5
    monedas=monedas-res5
    mon1=monedas/1
    mon1=floor(mon1)
    print("La cantidad de monedas de 10: ", mon10)
    print("La cantidad de monedas de 5: ", mon5)
    print("La cantidad de monedas de 1: ", mon1)

mon=int(input("Dame la cantidad de monedas: "))
conv(mon)
