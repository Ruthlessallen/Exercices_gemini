def celsius_a_fahrenheit(celsius):
    return (celsius*(9/5))+32
    
def fahrentheit_a_celsius(fahrenheit):
    return (fahrenheit-32)*(5/9)

ejecucion = True
while ejecucion == True:
    print("MENU DE CONVERSIONES")
    print("1. Convertir a F")
    print("2. Convertir a C")
    print("3. Salir")
    numero = input ("Elige: ")
    if numero == "1":
        celsius = float(input("Escribe el numero celsius para convertir: "))
        resultado = celsius_a_fahrenheit(celsius)
        print(f"Fahrenheit: {resultado}")
    elif numero =="2":
        fahrenheit = float(input("Escribe el numero fahrenheit para convertir: "))
        resultado = fahrentheit_a_celsius(fahrenheit)
        print(f"Celsius: {resultado}")
    elif numero == "3":
        ejecucion = False
print("saliendo del menu de conversiones.")
