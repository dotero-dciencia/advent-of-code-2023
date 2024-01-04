txt = open("AOC23\DIA3\PARTE1\input.txt")
entrada = txt.readlines()

lstNumeros = []
lstSimbolos = []
total = 0
fila = len(entrada)

for a in range (len(entrada)):
    entrada[a] = entrada[a].strip()
    controlDigitos = 0
    numero = ""
    for b in range(len(entrada[a])):
        if not entrada[a][b].isdigit() and entrada[a][b] != ".":
            if controlDigitos:
                lstNumeros.append((numero, entrada[a].index(numero)+a*fila))
                controlDigitos = 0
                numero = ""
            lstSimbolos.append(a*fila+b)
        elif entrada[a][b].isdigit():
            if controlDigitos: 
                numero += entrada[a][b]
            else:
                controlDigitos = 1
                numero = entrada[a][b]
        elif entrada[a][b] == ".":
            if controlDigitos:
                lstNumeros.append((numero, entrada[a].index(numero)+a*fila))
                controlDigitos = 0
                numero = ""
for numero in lstNumeros:
    indice = int(numero[1])
    longitud = len(numero[0])
    indices = [indice-fila-1,
               indice-fila+longitud,
               indice-1,
               indice+longitud,
               indice+fila-1,
               indice+fila+longitud
               ]
    for c in range (longitud):
        indices.append(indice-fila+c)
        indices.append(indice+fila+c)
    control = 0
    for index in indices:
        if index in lstSimbolos:
            control = 1
            break
    if control:
        total += int(numero[0])

print(total)