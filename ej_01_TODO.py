def calcular_media_positivos(lista_numeros):
    suma_total = 0
    conteo_positivos = 0
    for i in (lista_numeros):
        if i >= 0:
            suma_total += i
            conteo_positivos +=1
    # TODO: Itera sobre la lista de numeros
    # TODO: Dentro del bucle, comprueba si el número actual es mayor o igual a cero
    # TODO: Si es positivo, añádelo a suma_total y incrementa conteo_positivos
    
    if conteo_positivos > 0:
        media_suma = suma_total/conteo_positivos 
        return media_suma
    else: return 0
    # TODO: Fuera del bucle, comprueba si conteo_positivos es mayor que 0
    # TODO: Si lo es, calcula y devuelve la media (suma_total / conteo_positivos)
    # TODO: Si no hay positivos, devuelve 0 para evitar divisiones por cero

lista_numeros = [10, -5, 20, 0, 15, -3]
media = calcular_media_positivos(lista_numeros)
print(f"La media de los positivos es: {media}")