precios = {
    'manzana': 1.5, 
    'banana': 0.75,
    'naranja': 1.2}

while True: 
    fruta = input("escribe la fruta a buscar: ")
    if fruta in precios:
        euros = precios.get(fruta)
        print(f"La {fruta} tiene un precio de {euros}")
        False
    else: 
        print("Fruta no disponible.")
        False
        break 