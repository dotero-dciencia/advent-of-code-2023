txt = open("AOC23\DIA2\PARTE2\input.txt")
entrada = txt.readlines()

resultadoFinal = 0

for i in range (len(entrada)):
    entrada[i]=entrada[i].strip()

colors = ["red", "green", "blue"]

for i in range (len(entrada)):
    a = entrada[i]
    sets = a.split(": ")[1].split("; ")
    id = int(a.split(":")[0].split(" ")[1])
    minimo = [0, 0, 0]
    for a in range(len(sets)):
        sets[a] = sets[a].split(", ")
        for b in range (len(sets[a])):
            for c in range (len(colors)):
                if colors[c] in sets[a][b] and int(sets[a][b].split(" ")[0])>minimo[c]:
                    minimo[c] = int(sets[a][b].split(" ")[0])
                    break
    resultadoFinal += minimo[0]*minimo[1]*minimo[2]
print(resultadoFinal)