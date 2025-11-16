def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if (numero % i) == 0:
            return True
    return False # Error aquí, la indentación hace que solo funcione para el 2 y 3

for numero in range(0, 100):
    primo = es_primo(numero)
    print(numero, primo)