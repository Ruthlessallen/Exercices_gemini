numeros_pares = [2, 4, 6]
numeros_impares = [1, 3, 5]
todos_los_numeros = numeros_impares + numeros_pares
numeros_pares.extend(numeros_impares)
print(numeros_pares)
print(todos_los_numeros)