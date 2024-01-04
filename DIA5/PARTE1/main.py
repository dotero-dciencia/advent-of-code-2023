txt = open("AOC23\DIA5\PARTE1\input.txt")
entrada = txt.readlines()

for a in range(len(entrada)):
    entrada[a] = entrada[a].strip()

#Definimos lst como la lista con todas las semillas
lst = entrada[0].split(" ")
lst.pop(0)

lstMensajes = ["seed-to-soil map:", "soil-to-fertilizer map:", "fertilizer-to-water map:", "water-to-light map:","light-to-temperature map:","temperature-to-humidity map:","humidity-to-location map:"]

print(entrada.index(lstMensajes[0]))

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
    for b in range (len(lst)):
        for c in range (len(sources)):
            if sources[c][1] <= int(lst[b]) <= sources[c][2]:
                print(lst[b], sources[c][0])
                lst[b] = int(lst[b])+sources[c][0]
                break

lst.sort()
print(lst[0])