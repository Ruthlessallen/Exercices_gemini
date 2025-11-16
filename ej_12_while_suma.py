ejecucion = True
suma_total = 0
while True:
    user_numeros = input("escribe un numero o fin: ")
    if user_numeros == "fin":
        break
    user_numeros_int = int(user_numeros)
    suma_total += user_numeros_int
    print(f"el numero es {suma_total}")