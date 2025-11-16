def es_primo(numero):
    """Verifica si un solo número es primo."""
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if (numero % i) == 0:
            return False
    return True

# --- Tu código de práctica empieza aquí ---
inicio = input("Di un numero para empezar: ")
num_inicio = int(inicio)
final = input("Di un numero para finalizar: ")
num_final = int(final)
if num_inicio < 0:
    print("No es numero valido, tiene que ser positivo")
elif num_final > 1000:
    print("El numero tiene que ser menor a 1000")
for numero in range(num_inicio, num_final +1):
    if es_primo(numero):
        print(numero)