txt = open("AOC23\DIA4\PARTE1\input.txt")
entrada = txt.readlines()
total = 0

for i in range (len(entrada)):
    entrada[i] = entrada[i].strip()

for a in range (len(entrada)):
    string = entrada[a].split(": ")[1].split(" | ")
    cartasGanadoras = string[0].split(" ")
    misCartas = string[1].split(" ")
    recuento = 0
    for b in range (len(cartasGanadoras)):
        if cartasGanadoras == " ":
            cartasGanadoras.pop(b)
    for b in range (len(misCartas)):
        if misCartas[b].isdigit():
            if misCartas[b] in cartasGanadoras:
                print(misCartas[b])
                recuento += 1
    print(recuento)            
    if recuento > 0:
        total += 2**(recuento-1)
print(total)