def revertir_lista(lista):
    n_lista = []
    for i in range(len(lista)-1, -1, -1):
        n_lista.append(lista[i])
    return n_lista


lista = [1, 3, 5, 8, 9]
print(revertir_lista(lista))