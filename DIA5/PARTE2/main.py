txt = open("AOC23\DIA5\PARTE2\input.txt")
entrada = txt.readlines()

for a in range(len(entrada)):
    entrada[a] = entrada[a].strip()

#Definimos lst como la lista con todas las semillas
primeraLinea = entrada[0].split(" ")
primeraLinea.pop(0)

lst = []
for a in range (0, len(primeraLinea), 2):
    lst.append((int(primeraLinea[a]), int(primeraLinea[a])+int(primeraLinea[a+1])-1))
lstMensajes = ["seed-to-soil map:", "soil-to-fertilizer map:", "fertilizer-to-water map:", "water-to-light map:","light-to-temperature map:","temperature-to-humidity map:","humidity-to-location map:"]

for a in range (len(lstMensajes)):
    contador = 1
    indice = entrada.index(lstMensajes[a])
    sources = []
    while True:
        if len(entrada) > indice+contador:
            if entrada[indice+contador]==" " or entrada[indice+contador]=="":
                break
            else:
                linea = entrada[indice+contador].split(" ")
                for b in range (len(linea)):
                    linea[b] = int(linea[b])
                diferencia = linea[0]-linea[1]
                minimo = linea[1]
                maximo = linea[1]+linea[2]-1
                sources.append([diferencia, minimo, maximo])
                contador += 1
        else:
            break
    longitud = len(lst)
    for b in range (longitud):
        for c in range (len(sources)):
            n0 = lst[b][0]
            n1 = lst[b][1]
            diferencia = sources[c][0]
            minimo = sources[c][1]
            maximo = sources[c][2]
            if n0 <= minimo <= maximo <= n1:
                lst.append((minimo+diferencia, maximo+diferencia))
                if n1-maximo >= 1:
                    lst.append((maximo+1, n1))
                if minimo-n0 >= 1:
                    lst[b]=(n0, minimo-1)
                break
            elif n0 <= minimo <= n1:
                lst.append((minimo+diferencia, n1+diferencia))
                if minimo-n0 >= 1:
                    lst[b]=(n0, minimo-1)
                break
            elif n0 <= maximo <= n1:
                lst.append((n0+diferencia, maximo+diferencia))
                if n1-maximo >= 1:
                    lst[b]=(maximo+1, n1)
                break
        

lst.sort()
print(lst)
print(lst[0][0])