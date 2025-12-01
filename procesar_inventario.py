def procesar_inventario(fruteria):
    datos_fruteria = fruteria.split(",")
    l_fruta = []
    l_precio = []
    l_cantidad = []
    l_costo_total = []

    for i in range (0, len(datos_fruteria), 3):
        l_fruta.append(datos_fruteria[i])
        l_precio.append(datos_fruteria[i+1])
        l_cantidad.append(int(datos_fruteria[i+2].strip()))
        costo_total = float(datos_fruteria[i+1])*int(datos_fruteria[i+2].strip())
        l_costo_total.append(costo_total)
    
    suma = sum(l_costo_total)
    total_cantidad = sum(l_cantidad)
    suma_cantidad = suma / total_cantidad
    
    return l_fruta, l_precio, l_cantidad, l_costo_total, suma, suma_cantidad

fruteria = "manzana, 1.50, 15, platano, 2.00, 30, pera, 1.25, 45, uva, 3.40, 7"
l_fruta, l_precio, l_cantidad, l_costo_total, suma, suma_cantidad = procesar_inventario(fruteria)
print(f"La lista de frutas es {l_fruta}, cada fruta tiene precio de {l_precio}€, y existen {l_cantidad} unidades de cada. Si comprases la caja de un tipo de fruta sería {l_costo_total}")
print(f"Si quisieras comprar toda la fruteria te costaría: {suma}, por cada pieza de fruta estarias pagando {suma_cantidad}€")