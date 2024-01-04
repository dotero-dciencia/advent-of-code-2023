# Lectura de archivo en formato lista [linea1, linea2, linea3...]
txt = open("AOC23\DIA1\input.txt")
entrada = txt.readlines()

# Definición de la variable total a 0, que será la salida
total = 0

# Por cada línea
for i in range (len(entrada)):

    # Definición de lista para introducir todos los dígitos
    lst = []

    # Por cada caracter de la línea
    for a in range (len(entrada[i])):

        # ¿Es dígito?
        if entrada[i][a].isdigit():

            # Añadir a la lista
            lst.append(entrada[i][a])

    # Sumar a total la concatenación del primer elemento y último de la lista
    total += int(lst[0]+lst[-1])

# Salida
print(total)