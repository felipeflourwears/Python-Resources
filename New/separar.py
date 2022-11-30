stringc="separado"
for i in range(0,len(stringc),1):
    remplazo=''
    remplazo=stringc[i].replace("", ",")
print(remplazo)

# palabra = "Separado"
# print(palabra)

# reemplazar = palabra.replace("" , ",")
# print(reemplazar)

print("Nueva implementacion")
listaseparada=stringc
h=list(listaseparada)
print(type(h))
print(h)
pString = ','.join(listaseparada)
print(pString)

print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

print('I\'m Monty Python.')