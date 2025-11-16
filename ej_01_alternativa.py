def sumar_numeros(lista_nums):
    total = 0
    for num in lista_nums:
        total += num
    return total

numeros_error1 = [10, 20, 30, 40] # Debería sumar 100
print(f"La suma total es: {sumar_numeros(numeros_error1)}")