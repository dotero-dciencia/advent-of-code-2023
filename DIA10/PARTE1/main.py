txt = open("AOC23\DIA10\PARTE1\input2.txt")
entrada = txt.readlines()
matrizTubos = []
matrizValores = []
tubosPorRecorrer = []

#Lectura del fichero. Creación de la matriz.
for a in range (len(entrada)):
    entrada[a] = entrada[a].strip()
    linea = entrada[a]
    fila = []
    filaValores = []
    for b in range (len(linea)):
        fila.append(linea[b])
        filaValores.append(0)
        if linea[b] == "S":
            posicionS = [a, b]
    matrizTubos.append(fila)
    matrizValores.append(filaValores)

#Asignación de posibles tubos alrededor de la posición de salida.
posiblesTubos = {"P1": ["|", "7", "F"], "P2": ["-", "L", "F"], "P3": ["-", "7", "J"], "P4": ["|", "L", "J"]}

#Lectura de los tubos alrededor de la posición de salida.
tubo1, tubo2, tubo3, tubo4 = matrizTubos[posicionS[0]-1][posicionS[1]], matrizTubos[posicionS[0]][posicionS[1]-1], matrizTubos[posicionS[0]][posicionS[1]+1], matrizTubos[posicionS[0]+1][posicionS[1]]

#Asignación de las posiciones con las que conecta cada tubo
conexionesTubos = {"|":[[1, 0],[-1,0]],
                   "-":[[0, 1],[0,-1]],
                   "L":[[1, 0],[0,1]],
                   "J":[[1, 0],[0,-1]],
                   "7":[[-1, 0],[0,-1]],
                   "F":[[-1, 0],[0,1]]}

#Comprobación de qué tubos son correctos en la posición de salida.
if tubo1 in posiblesTubos.get("P1"):
    matrizValores[posicionS[0]-1][posicionS[1]] = 1
    tubosPorRecorrer.append([tubo1, [posicionS[0]-1,posicionS[1]], 1])
if tubo2 in posiblesTubos.get("P2"):
    matrizValores[posicionS[0]][posicionS[1]-1] = 1
    tubosPorRecorrer.append([tubo2, [posicionS[0],posicionS[1]-1], 1])
if tubo3 in posiblesTubos.get("P3"):
    matrizValores[posicionS[0]][posicionS[1]+1] = 1
    tubosPorRecorrer.append([tubo3, [posicionS[0],posicionS[1]+1], 1])
if tubo4 in posiblesTubos.get("P4"):
    matrizValores[posicionS[0]+1][posicionS[1]] = 1
    tubosPorRecorrer.append([tubo4, [posicionS[0]+1,posicionS[1]], 1])

#

while len(tubosPorRecorrer) > 0:
    tubo = tubosPorRecorrer[0][0]
    posPrimerTubo = [tubosPorRecorrer[0][1][0]+conexionesTubos.get(tubo)[0][0],tubosPorRecorrer[0][1][1]+conexionesTubos.get(tubo)[0][1]]
    posSegundoTubo = [tubosPorRecorrer[0][1][0]+conexionesTubos.get(tubo)[1][0],tubosPorRecorrer[0][1][1]+conexionesTubos.get(tubo)[1][1]]
    if posPrimerTubo [0] >= 1 and posPrimerTubo[1] >= 1 :
        primerTubo = matrizTubos[posPrimerTubo[0]][posPrimerTubo[1]]
    segundoTubo = matrizTubos[posSegundoTubo[0]][posSegundoTubo[1]]
    tubosCorrespondientes = [primerTubo, segundoTubo]
    if matrizValores[posPrimerTubo[0]][posPrimerTubo[1]] == 0 and matrizTubos[posPrimerTubo[0]][posPrimerTubo[1]] != "S":
        matrizValores[posPrimerTubo[0]][posPrimerTubo[1]] = tubosPorRecorrer[0][2]+1
        tubosPorRecorrer.append([tubosCorrespondientes[0], [posPrimerTubo[0], posPrimerTubo[1]], tubosPorRecorrer[0][2]+1])
    if matrizValores[posSegundoTubo[0]][posSegundoTubo[1]] == 0 and matrizTubos[posSegundoTubo[0]][posSegundoTubo[1]] != "S": 
        matrizValores[posSegundoTubo[0]][posSegundoTubo[1]] = tubosPorRecorrer[0][2]+1
        tubosPorRecorrer.append([tubosCorrespondientes[1], [posSegundoTubo[0], posSegundoTubo[1]], tubosPorRecorrer[0][2]+1])
    print(len(tubosPorRecorrer), tubosPorRecorrer)
    tubosPorRecorrer.pop(0)

valorMaximo = 0

for linea in matrizValores:
    for elemento in linea:
        if elemento >= valorMaximo:
            valorMaximo = elemento

print(valorMaximo)