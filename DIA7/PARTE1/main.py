def subListas (lista):
    contador = 0
    while len(lista) >= 1:
        indice = lista[contador][0]
        for a in range(len(lst)):
            if lista[0][0] == indice:
                lst.append(lista[0])
                lista.pop(0)
            else:
                contador += 1
                break

def ordenarLista(lista, simbolos, ordenFinal):
    lst = []
    contador = 0
    while len(lista) >= 1:
        indice = lista[contador][0]
        for a in range(len(lst)):
            if lista[0][0] == indice:
                lst.append(lista[0])
                lista.pop(0)
            else:
                contador += 1
                break
            print(lst)
    print(lista, lst)
    if len(lst) > 1 and len(lst[0][1])>0:
        for a in range (len(lst)):
            lst[a][0] = simbolos.index(str(lst[a][1][0]))
            lst[a][1] = lst[a][1][1:]
        lst.sort()
        ordenFinal.append(ordenarLista(lst, simbolos, ordenFinal))
    else:
        ordenFinal.append(lst[0])
    return(ordenFinal)

txt = open("AOC23\DIA7\PARTE1\input.txt")
entrada = txt.readlines()

lst = []

combinacionesPosibles = [[5], [4, 1], [3, 2], [3, 1, 1], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1,]]
simbolos = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

for a in range (len(entrada)):
    entrada[a] = entrada[a].strip()
    mazo = entrada[a].split(" ")[0]
    multiplicador = entrada[a].split(" ")[1]
    caracteres = []
    combinacion = []
    for b in range (len(mazo)):
        if mazo[b] in caracteres:
            combinacion[caracteres.index(mazo[b])] += 1
        else:
            combinacion.append(1)
            caracteres.append(mazo[b])
    print(combinacion)
    combinacion.sort()
    combinacion.reverse()
    lst.append([combinacionesPosibles.index(combinacion), mazo, multiplicador])
lst.sort()


ordenFinal = []

ordenarLista(lst,simbolos,ordenFinal)


print(ordenFinal, len(ordenFinal), len(entrada))