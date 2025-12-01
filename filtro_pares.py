numeros = [12, 5, 8, 23, 16, 7, 30]

def filtrar_pares(numeros):
    numero_par = []
    for i in numeros:
        if i%2 == 0:
            numero_par.append(i)
    return numero_par

print(filtrar_pares(numeros))