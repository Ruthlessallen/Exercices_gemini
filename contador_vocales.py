texto = "Esto es UnA cadena de texto escrIta en visual studio code"
vocales = []
may = []
for i in texto:
    if i in "aeiou":
        vocales.append(i)
    elif i in "AEIUO":
        may.append(i)

print(len(vocales), len(may))

