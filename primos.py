import os

r = 250
suma = 0
#formula: (n-1)!+1 es multiplo de n
txt = ""

for x in range(2, r+1):
    for num in range(1, (x-1)):
        if suma == 0:
            suma += ((x-1)*(x-1-num))
        else:
            suma = suma*(x-1-num)
    


    if ((suma+1)%x == 0 or x==2):
            txt += f"{x}\n"
    suma = 0

file = open('resultado.txt', 'w')
file.write(txt)
file.close()
