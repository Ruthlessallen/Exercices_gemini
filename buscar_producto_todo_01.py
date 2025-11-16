inventario_muebles = {"Sillón": 3, "Lámpara": 15, "Espejo": 7}

# TODO: Define la función 'buscar_producto' con los dos parámetros requeridos.
def buscar_producto(producto, inventario_muebles):
        if producto in inventario_muebles:
            return inventario_muebles[producto]
        else: 
            return 0
        
buscador = buscar_producto('Espejo', inventario_muebles)
# TODO: La función debe usar un condicional para verificar si el 'nombre' es una clave en el 'inventario'.
# TODO: Si existe, debe retornar el valor asociado (la cantidad).
# TODO: Si NO existe, debe retornar 0.
# TODO: Imprime el resultado de buscar "Lámpara".
# TODO: Imprime el resultado de buscar "Alfombra".
print(buscador)

# Resultado esperado: 15 y 0.