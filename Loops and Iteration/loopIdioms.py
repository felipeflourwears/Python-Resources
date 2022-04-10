print("Before")
for thing in [9, 41, 12, 3, 74, 15]:
    print(thing)
print("After")

#El número más largo 3 41 12 9 74 15
#Para actualizar un dato
numLargest=0 
arrayNum=[3,41,12,9,74,15]
for i in arrayNum:
    if i>numLargest:
        numLargest=i
print("Number max: ", numLargest)

#Counting in a loop
rork=0
print('Before', rork)
for thing in [9, 41, 12, 3, 74, 15]:
    rork=rork+1
    print(rork, thing)
print('After', rork)

        