import random
numero_secreto = random.randint(1, 20)
intentos_maximos = 3
intentos_actuales = 0
ganar = False
numero_intento_maximo = intentos_maximos
print(f"tienes {numero_intento_maximo} intentos")

while intentos_actuales< intentos_maximos and ganar is False:
    intentos_actuales += 1
    numero_intento_maximo -=1
    intento = int(input("di un numero: "))
    if intento == numero_secreto:
        print("ganaste")
        ganar = True
    elif intento < numero_secreto:
        print("Incorrecto, el numero secreto es mayor")
        print(f"te quedan  {numero_intento_maximo} intentos")
    elif intento > numero_secreto:
        print("Incorrecto, el numero secreto es menor")
        print(f"te quedan  {numero_intento_maximo} intentos")
if ganar == False:
    print(f"has perdido, el numero es {numero_secreto}")