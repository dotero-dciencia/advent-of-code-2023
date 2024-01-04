txt = open("AOC23\DIA6\PARTE1\input.txt")
entrada = txt.readlines()

for a in range (len(entrada)):
    entrada[a] = entrada[a].strip()

milisegundos = entrada[0].split(" ")
milisegundos.pop(0)
milimetros = entrada[1].split(" ")
milimetros.pop(0)

lst = []
for a in range (len(milisegundos)):
    if not milisegundos[a] == " " and not milisegundos[a] == "":
        lst.append(int(milisegundos[a]))
milisegundos = lst

lst = []
for a in range (len(milimetros)):
    if not milimetros[a] == " " and not milimetros[a] == "":
        lst.append(int(milimetros[a]))
milimetros = lst

total = 1
for a in range (len(milisegundos)):
    contador = 0
    for b in range(int(milisegundos[a])):
        puntuacion = b*(milisegundos[a]-b)
        if puntuacion > milimetros[a]:
            contador += 1
    if contador >= 1:
        total *= contador
    print(contador)
print(total)