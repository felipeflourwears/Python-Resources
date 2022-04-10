def print_lyrics():
    print("Im luberjack, and Im OK")
x=5
print("Yo")
x=x+2
print(x)
print_lyrics()

#return value
def idioma(lengua):
    if (lengua=='Espanol' or lengua=='espanol'):
        return "Hola"
    elif (lengua=='Frances'or lengua=="frances"):
        return "Bonjur"
    else:
        return "Hello"



#Return value
def great():
    return "Hello"

def addTwo(x, y):
    added=x+y
    return added


print(great(), "LuisFe")
print(great(), "Caro")
xsum=addTwo(3,5)
print(xsum)
entrada=input("Dame el lenguaje: ")
print(idioma(entrada))


