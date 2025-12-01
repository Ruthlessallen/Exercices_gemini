import random

def verificar_parametros():
    n_aleatorio = [0]
    n_tupla = tuple(n_aleatorio)
    for i in range(10):
        n = random.randint(-50, 50)
        n_aleatorio.append(n)

    n_tupla = tuple(n_aleatorio)
    n_negativo = []
    n_positivo = []

    indice = 0
    while indice < len(n_tupla):
        n_actual = n_tupla[indice]
        if n_actual <= 0:
            n_negativo.append(n_actual)
        else:
            n_positivo.append(n_actual)
        indice += 1
    print(f"Verificando: {n_tupla}. numeros negativos: {n_negativo}. Numeros positivos: {n_positivo}")
    return len(n_negativo) == 0

verificar_parametros()