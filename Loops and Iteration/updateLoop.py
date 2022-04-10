#El número más largo 3 41 12 9 74 15
#Para actualizar un dato
numLargest=0 
arrayNum=[3,41,12,9,74,15]
for i in arrayNum:
    if i>numLargest:
        numLargest=i
print("Number max: ", numLargest)