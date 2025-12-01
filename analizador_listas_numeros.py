lista = [10, 20, 5, 3, 78, 63, 37, 22, 54, 76]

def analizar_lista(lista):
    suma = sum(lista)
    

    maximo = lista[0]
    for i in lista:
        if i > maximo: 
            maximo = i

    minimo = lista[0]
    for i in lista:
        if i < minimo: 
            minimo = i

    cantidad = len(lista)
    promedio = suma/cantidad

    return suma, maximo, minimo, promedio

suma, maximo, minimo, promedio = analizar_lista(lista)
print(f"La lista sumada es: {suma}. El número máximo es {maximo} y el mínimo es {minimo}. El promedio de la lista es {promedio}")