vocal=str(input("Dame una letra: ")).lower()
print("Me diste la letra: ", vocal)
def detvocal(vocal):
    dictionary="aeiou"
    passv=False
    for i in dictionary:
        if i==vocal:
            passv=True
    if passv==True:
        print("Es vocal")
    else:
        print("No es vocal") 
    
detvocal(vocal)

