total = 0
while True:
    numeros = int(input("Escribe numeros o escribe '0' para finalizar: "))
    total += numeros
    if numeros == 0:
        print(total)
        break