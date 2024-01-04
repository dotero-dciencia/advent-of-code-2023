txt = open("AOC23\DIA9\PARTE1\input.txt")
entrada = txt.readlines()
total = 0

for linea in entrada:
    linea = linea.strip()
    lst = []
    lst.append(linea.split(" "))
    for a in range (len(lst[0])):
        lst[0][a] = int(lst[0][a])
    for a in range (len(lst[0])):
        sublst = []
        maxValor = 0
        for b in range (len(lst[a])-1):
            sublst.append(lst[a][b+1]-lst[a][b])
            if lst[a][b+1]-lst[a][b] != maxValor:
                maxValor = float("inf")
        lst.append(sublst)
        if maxValor == 0:
            break
    ultimosValores = []
    for a in range (len(lst)):
        if len(lst[a]) >= 1:
            ultimosValores.append(lst[a][0])
    ultimosValores.reverse()
    for a in range (len(ultimosValores)-1):
        ultimosValores[a+1]=ultimosValores[a+1]-ultimosValores[a]
    total += ultimosValores[-1]

print(total)