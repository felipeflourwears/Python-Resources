print('Before')
arrayNum=[9, 41, 12, 3, 74, 15]
for value in arrayNum:
    if value>20:
        print('Large Number', value)
print('After')


print('Before')
arrayNum=[9, 41, 12, 3, 74, 15]
arrayMin=[]
arrayMax=[]
for value in arrayNum:
    if value>20:
        print('Large Number(20)', value)
        arrayMax.append(value)
        arrayMax.sort()
    elif value<20:
        print('Short Number(20)', value)
        arrayMin.append(value)
        arrayMin.sort()
print('After')
print("Imprimiendo arreglo mayor a 20")
print(arrayMax)
print("Imprimiendo arreglo menor a 20")
print(arrayMin)