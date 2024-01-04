txt = open("AOC23\DIA2\PARTE1\input.txt")
entrada = txt.readlines()

resultadoFinal = 0

for i in range (len(entrada)):
    entrada[i]=entrada[i].strip()

colors = ["blue", "red", "green"]
valorMaximo = [14, 12, 13]

for i in range (len(entrada)):
    a = entrada[i]
    sets = a.split(": ")[1].split("; ")
    id = int(a.split(":")[0].split(" ")[1])
    valido = 1
    for a in range(len(sets)):
        sets[a] = sets[a].split(", ")
        print(sets[a])
        for b in range (len(sets[a])):
            for c in range (len(colors)):
                if colors[c] in sets[a][b] and int(sets[a][b].split(" ")[0])>valorMaximo[c]:
                    valido = 0
                    break
    if valido:
        resultadoFinal += id
print(resultadoFinal)