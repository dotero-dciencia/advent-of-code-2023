import re

# Lectura del archivo en formato lista (línea1, línea2...)
txt = open("AOC23\DIA1\PARTE2\input.txt")
entrada = txt.readlines()

# Por cada elemento de la lista, eliminar \n
for i in range (len(entrada)):
    entrada[i]=entrada[i].strip()
cont=0
for e in entrada:
    dnis_validos=re.findall("one|two|three|four|five|six|seven|eight|nine|\d", e)
    string_final=""
    for i in [dnis_validos[0],dnis_validos[-1]]:
        match i:
            case "one":
                string_final+="1"
            case "two":
                string_final+="2"
            case "three":
                string_final+="3"
            case "four":
                string_final+="4"
            case "five":
                string_final+="5"
            case "six":
                string_final+="6"
            case "seven":
                string_final+="7"
            case "eight":
                string_final+="8"
            case "nine":
                string_final+="9"
            case _:
                string_final+=i
    print(string_final)
    cont+=int(string_final)
print(cont)