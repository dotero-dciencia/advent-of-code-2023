txt = open("AOC23\DIA4\PARTE2\in.txt")
entrada = txt.readlines()
total = 0
lstCartas = []

for i in range (len(entrada)):
    entrada[i] = entrada[i].strip()
    lstCartas.append(1)

for a in range (len(entrada)):
    stringInicial = entrada[a].split(": ")
    string = stringInicial[1].split(" | ")
    id = int(stringInicial[0].split(" ")[-1])
    cartasGanadoras = string[0].split(" ")
    misCartas = string[1].split(" ")
    recuento = 0
    for b in range (len(cartasGanadoras)):
        if cartasGanadoras == " ":
            cartasGanadoras.pop(b)
    for b in range (len(misCartas)):
        if misCartas[b].isdigit():
            if misCartas[b] in cartasGanadoras:
                recuento += 1
    for b in range (recuento):
        lstCartas[b+id] += lstCartas[id-1]
for a in range (len(lstCartas)):
    total += int(lstCartas[a])
print(total)