import re

# Lectura del archivo en formato lista (línea1, línea2...)
txt = open("AOC23\DIA1\PARTE2\input.txt")
entrada = txt.readlines()

# Por cada elemento de la lista, eliminar \n
for i in range (len(entrada)):
    entrada[i]=entrada[i].strip()

# Asignar total a 0, que será la salida y definición de los posibles números escritos en la lista lstStrings
total = 0
dic = {"one":"on1e", "two":"tw2o", "three":"thre3e", "four":"fou4r", "five":"fiv5e", "six":"si6x", "seven":"seve7n", "eight":"eigh8t", "nine":"nin9e"}

for elemento in entrada:
    lst=[]
    for key in dic.keys():
        elemento = elemento.replace(key,dic.get(key))
    print(elemento)
    # Por cada caracter de la línea
    for a in range (len(elemento)):
        # ¿Es dígito?
        if elemento[a].isdigit():
            # Añadir a la lista
            lst.append(elemento[a])

    # Sumar a total la concatenación del primer elemento y último de la lista
    total += int(lst[0]+lst[-1])

print(total)