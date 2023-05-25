import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

n = int(input("Introduce el número de observaciones: "))

x = []
y = []

print("\nIntroduce los valores de x: ")
for i in range(n):
    x.append(float(input("Valor de x[{}]: ".format(i))))

print("\nIntroduce los valores de y: ")
for i in range(n):
    y.append(float(input("Valor de y[{}]: ".format(i))))

print("\nValores de x:", x)
print("Valores de y:", y)


# Calcular la media de x e y
sum_x = sum(x)
sum_y = sum(y)

media_x = sum_x / n
media_y = sum_y / n

print("Media de x:", media_x)
print("Media de y:", media_y)


# Calcular la pendiente y el intercepto de la recta de regresión
numer = 0
denom = 0

for i in range(n):
    numer += (x[i] - media_x) * (y[i] - media_y)
    denom += (x[i] - media_x) ** 2

pendiente = numer / denom
intercepto = media_y - pendiente * media_x

print("Pendiente:", pendiente)
print("Intercepto:", intercepto)


# Imprimir los resultados
print(f"La ecuación de la recta de regresión es y = {pendiente}x + {intercepto}")


# Graficar los puntos y la recta de regresión
plt.scatter(x, y)
plt.plot(x, pendiente * np.array(x) + intercepto, color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regresión lineal')
plt.show()