numero_valido = False
edad = 0
while not numero_valido:
    entrada = input("¿Cuántos años tienes? (debe ser positivo): ")
    if entrada.isdigit():
        entero = int(entrada)
        if entero > 0:
            edad += entero
            numero_valido = True 
        else:
            print("No es valido")
    else:
        print("tiene que ser digito")
    # TODO: Comprueba si la entrada es un dígito usando .isdigit()
    # TODO: Si es un dígito, conviértelo a entero y comprueba si es > 0
    # TODO: Si es válido, establece numero_valido a True y guarda la edad
    # TODO: Si no es válido, imprime un mensaje de error y el bucle continuará

print(f"Edad válida introducida: {edad}")