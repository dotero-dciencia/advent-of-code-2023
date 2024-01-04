txt = open("AOC23\DIA11\PARTE1\input2.txt")
entrada = txt.readlines()

# 1. Convertir a matriz la entrada

matriz = []
for linea in entrada:
    linea = linea.strip()
    fila = []
    for elemento in linea:
        fila.append(elemento)
    matriz.append(fila)

# 2. Duplicar las filas y columnas cuyos elementos sean solamente "."
    
# 2.1. Duplicar filas

posicion = 0
posicionesDuplicar = []
for linea in matriz:
    contador = 0
    for elemento in linea:
        if elemento == ".":
            contador += 1
    if contador == len(linea):
        posicionesDuplicar.append(posicion)
        ejemplo = linea
    posicion += 1

for posicionDuplicar in posicionesDuplicar:
    matriz.insert(posicionDuplicar, ejemplo)

# 2.2. Duplicar columnas
    
posicion = 0
posicionesDuplicar = []
for a in range (len(matriz[0])):
    columna = []
    for b in range (len(matriz)):
        columna.append(matriz[b][a])
    contador = 0
    for elemento in columna:
        if elemento == ".":
            contador += 1
    if contador == len(columna):
        posicionesDuplicar.append(posicion)
    posicion += 1

for a in range (len(matriz)):
    for posicionDuplicar in posicionesDuplicar:
        matriz[a].insert(posicionDuplicar, ".")

# 3. Encontrar todas las galaxias. Introducirlas en una lista con ID y posición

galaxias = []    
for a in range (len(matriz)):
    for b in range (len(matriz[a])):
        if matriz[a][b] == "#":
            galaxias.append((a, b))

# 4. Encontrar todas las parejas entre galaxias

parejas = []
for a in range (len(galaxias)):
    for b in range (len(galaxias)-1):
        parejas.append((galaxias[0], galaxias[b+1]))
    galaxias.pop(0)

# 5. Calcular distancia mínima entre cada par de galaxias con la formula d = | f1 - f2 | + | c1 - c2 | 
    
total = 0

for pareja in parejas:
    valoresFilas = [pareja[0][0], pareja[1][0]]
    valoresColumnas = [pareja[0][1], pareja[1][1]]
    valoresFilas.sort()
    valoresColumnas.sort()
    diferenciaFilas = valoresFilas[1]-valoresFilas[0]
    diferenciaColumnas = valoresColumnas[1]-valoresColumnas[0]
    total += diferenciaFilas + diferenciaColumnas
print(total)