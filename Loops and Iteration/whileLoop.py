
#Ir del 5 para abajo
n=5
while n>0:
    print(n)
    n=n-1
print('Blastoff')
print(n)

#Loop con while True
while True:
    line=input('input: done>>')
    if line =='done':
        break
    print(line)
print('Done')

while True:
    line=input('Entrada: Hecho>>')
    if line[0] =='continue':
        continue
    if line=='Hecho':
        break
    print(line)
print('Hecho!')
