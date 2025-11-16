suma_total = 0
while True:
    numero = int(input("escribe un numero: "))
    if numero >= 0:
        suma_total += numero
        print(suma_total)
    elif numero <= 0:
        print("fin")
        break