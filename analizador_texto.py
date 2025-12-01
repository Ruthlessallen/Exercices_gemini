texto = "El Python es un lenguaje de programación muy popular. El lenguaje es fácil de aprender.".lower().replace(".", "") #texto en minuscula, quitando los puntios

l_texto = texto.split(" ")#texto splited en una variable

frecuencias = {

}#diccionario

for i in l_texto:
    numeros = frecuencias.get(i, 0)
    n_numero =numeros +1
    frecuencias[i] =n_numero

print(frecuencias)#printea dict