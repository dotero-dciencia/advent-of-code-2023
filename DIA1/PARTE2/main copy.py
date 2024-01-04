# Lectura del archivo en formato lista (línea1, línea2...)
txt = open("AOC23\DIA1\PARTE2\input.txt")
entrada = txt.readlines()

# Por cada elemento de la lista, eliminar \n
for i in range (len(entrada)):
    entrada[i]=entrada[i].strip()

# Asignar total a 0, que será la salida y definición de los posibles números escritos en la lista lstStrings
total = 0
lstStrings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# Por cada línea
for i in range (len(entrada)):

    # Definimos una lista, que contendrá los dígitos
    lst = []

    # FUNCIÓN 1: Por cada caracter, añadir a la lista si es dígito.
    for a in range (len(entrada[i])):
        if entrada[i][a].isdigit():
            lst.append(entrada[i][a])

    # FUNCIÓN 2: Por cada número que puede aparecer como String
    for b in range (len(lstStrings)):

        # Cuántas veces aparece el string en la línea
        repeticiones = entrada[i].count(lstStrings[b])

        # Por cada vez que aparece el string en la línea
        for c in range (repeticiones):

            # Posición del string en la línea
            indice = entrada[i].index(lstStrings[b])
            # ¿Está antes que el primer número de la lista? Si es así, insertar el primero
            if indice < entrada[i].index(lst[0]):
                lst.insert(0, lstStrings[b])
            elif indice > entrada[i].index(lst[-1]):
                lst.append(lstStrings[b])
    
    # Sumar a total la concatenación del primer dígito y el último de la lista
    for d in range (len(lst)):
        if not lst[d].isdigit():
            lst[d] = str(lstStrings.index(lst[d])+1)
    total += int(lst[0] + lst[-1])

# Salida
print(total)