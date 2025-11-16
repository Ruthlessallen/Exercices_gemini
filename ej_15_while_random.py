import random
limite = 200
suma_acumulada = 0
while True:
    numero = random.randint(0, 200)
    if suma_acumulada +numero <= limite:
        suma_acumulada += numero
        print(suma_acumulada)
    else:
        break