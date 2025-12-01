def calcular_descuento(precio_original, porcentaje_descuento):
    descuento_total = precio_original * porcentaje_descuento / 100
    print(f"El descuento es de {descuento_total} euros")
    precio_final = precio_original - descuento_total
    if porcentaje_descuento > 20:
        precio_final -= 5
    print(f"El precio final con el descuento es de {precio_final}")
    return precio_final

precio_original = float(input("Escribe el precio: "))
porcentaje_descuento = float(input("Escribe de 0 a 100 el porcentaje de descuento: "))
total = calcular_descuento(precio_original, porcentaje_descuento)
