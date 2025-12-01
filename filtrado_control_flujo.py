palabras = ["rojo", "verde", "azul", "negro", "blanco", "amarillo", "gris"]

for i in palabras: #itera sobre la lista
    if i == "blanco": #si la palabra iterada (i) es igual a "blanco"
        print(i)#printea la palabra
        break#y ahora para

    elif len(i) < 5: #si la longitud de la palabra iterada es menor a 5
        continue #continua y no la imprimas

    else:  #si no es blanco, ni tiene menos de 5 palabras entonces
        print(f"Palabra de 5 letras: {i}") #printea la palabra iterada (que no sera ni blanco ni menor de 5 letras)