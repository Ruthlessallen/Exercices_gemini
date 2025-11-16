PIN_SECRETO = str("0505")
intentos_maximos = 3
intentos_actuales = 0
codigo_correcto = False

while intentos_actuales < intentos_maximos and codigo_correcto is False:
    intentos_actuales += 1
    intento = str(input("Escribe el codigo pin: "))
    if intento == PIN_SECRETO:
        codigo_correcto = True
        print("Codigo correcto")
    elif intento != PIN_SECRETO:
        intentos_restantes = intentos_maximos - intentos_actuales
        print(f"Codigo incorrecto")
if codigo_correcto == False:
    print("Te has quedado sin intentos")