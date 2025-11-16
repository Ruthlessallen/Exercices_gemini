ejecutando = True
while ejecutando == True:
    print("Menú: 1. Inicio, 4. Salir")
    opcion = input("Elige: ")
    if opcion == "4":
        ejecutando = False
        break # Error aquí
    elif opcion == "1":
        print("Iniciando...")
print("Saliendo")  

# Falta el mensaje final, el bucle nunca termina correctamente