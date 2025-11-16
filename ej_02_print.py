cuenta = float(input("La cuenta es de: "))
propina = float(input("El % de propina es de: "))

total_propina = cuenta * (propina/100)
print(f"La propina es de {total_propina}")
total_cuenta = cuenta + total_propina
print(f"El total de la cuenta es {total_cuenta}")

division = int(input("La cuenta se divide entre: "))
division_cuenta = total_cuenta / division
print(f"Se divide entre {division} y cada uno tiene que pagar {division_cuenta}")