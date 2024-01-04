txt = open("AOC23\DIA8\PARTE2\input.txt")
entrada = txt.readlines()

for i in range (len(entrada)):
    entrada[i] = entrada[i].strip()

nodos = {}
instrucciones = entrada[0]
entrada.pop(0)
entrada.pop(0)
traducir = ['L', 'R']
direcciones = []

for i in range (len(instrucciones)):
    direcciones.append(traducir.index(instrucciones[i]))

for linea in entrada:
    print(linea)
    linea = linea.split(" ")
    nombreNodo = linea[0]
    conexionesNodo = [linea[2], linea[3]]
    conexionesNodo[0],conexionesNodo[1]= conexionesNodo[0][1]+conexionesNodo[0][2]+conexionesNodo[0][3], conexionesNodo[1][0] + conexionesNodo[1][1] + conexionesNodo[1][2]
    nodos[nombreNodo] = (conexionesNodo[0], conexionesNodo[1])

nodosActuales = []
lstNodos = nodos.keys()

for nodo in lstNodos:
    if nodo[2] == "A":
        nodosActuales.append(nodo)
print(nodosActuales)

iterador = 0
contador = 0
while True:
    for a in range (len(nodosActuales)):
        nodosActuales[a] = nodos.get(nodosActuales[a])[direcciones[iterador%len(direcciones)]]
        if nodosActuales[a][2] == "Z":
            contador += 1
            print(contador, len(nodosActuales))
    if contador > 3:#len(nodosActuales):
        print(iterador+1)
        break
    else:
        iterador+=1
        contador = 0