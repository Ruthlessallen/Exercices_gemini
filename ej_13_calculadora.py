def sumar(a, b):
    resultado_suma = a + b
    return resultado_suma

def resta(a, b):
    resultado_resta = a - b
    return resultado_resta

def multiplicacion(a, b):
    resultado_multi = a * b
    return resultado_multi

def division(a, b):
    resultado_division = a / b
    return resultado_division

while True:
    print("MENU:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multi")
    print("4. Division")
    print("0. Salir")
    choice = input("Elige usando los numeros.").strip()
    if choice == "1":
        a = int(input("elige el primer numero"))
        b = int(input("elige el segundo numero"))
        resultado = sumar(a, b)
        print(resultado)
    elif choice == "2":
        a = int(input("elige el primer numero"))
        b = int(input("elige el segundo numero"))
        resultado = resta(a, b)    
        print(resultado)
    elif choice == "3":
        a = int(input("elige el primer numero"))
        b = int(input("elige el segundo numero"))
        resultado = multiplicacion(a, b)    
        print(resultado)
    elif choice == "4":
        a = int(input("elige el primer numero"))
        b = int(input("elige el segundo numero"))
        resultado = division(a, b)   
        print(resultado) 
    elif choice == "0":
        print("Saliendo")
        break