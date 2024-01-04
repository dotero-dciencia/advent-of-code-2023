txt = open("AOC23\DIA6\PARTE1\input.txt")
entrada = txt.readlines()

for a in range (len(entrada)):
    entrada[a] = entrada[a].strip()

milisegundos = entrada[0].split(" ")
milisegundos.pop(0)
milimetros = entrada[1].split(" ")
milimetros.pop(0)

ms = ""
for a in range (len(milisegundos)):
    if not milisegundos[a] == " " and not milisegundos[a] == "":
        ms += str(milisegundos[a])

mm = ""
for a in range (len(milimetros)):
    if not milimetros[a] == " " and not milimetros[a] == "":
        mm += str(milimetros[a])

mm, ms = int(mm), int(ms)

contador = 0
for b in range(int(ms)):
    puntuacion = b*(ms-b)
    if puntuacion > mm:
        contador += 1
print(contador)
