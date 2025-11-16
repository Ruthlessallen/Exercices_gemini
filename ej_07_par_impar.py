def clasificar_numeros(lista_de_numeros):
    par = 0
    impar = 0
    lista_impar = []
    lista_par = []
    for i in lista_de_numeros:
        if i % 2 == 0:
            par += 1
            lista_par.append(i)
        else:
            impar += 1
            lista_impar.append(i)
    return par, impar, lista_impar, lista_par

numero = input("Escribe 8 numeros para saber cuantos son pares e impares usando comas: ").split(',')
lista_de_numeros = []
for i in numero:
    lista_de_numeros.append(int(i))
conteo_par, conteo_impar, impar, par = clasificar_numeros(lista_de_numeros)
print (f"hay {conteo_par} pares y son {par} y {conteo_impar} impares y son {impar}")