txt = open("AOC23\DIA8\PARTE1\input.txt")
entrada = txt.readlines()

for i in range (len(entrada)):
    entrada[i] = entrada[i].strip()

nodos = {}
nodoActual = 'AAA'
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
print(nodos)


iterador = 0
while True:
    nodoActual = nodos.get(nodoActual)[direcciones[iterador%len(direcciones)]]
    print(nodoActual, nodos.get(nodoActual), direcciones[iterador%len(direcciones)])
    if nodoActual == 'ZZZ':
        print(iterador+1)
        break
    else:
        iterador+=1