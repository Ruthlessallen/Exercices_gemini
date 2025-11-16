inventario_ropa = {"Calcetines": 50, "Gorra": 30, "Bufanda": 20}
productos_a_actualizar = [
    ("Gorra", 15),       # Esta sí debe actualizarse
    ("Calcetines", 60),  # Esta sí debe actualizarse
    ("Guantes", 10)      # Este producto NO existe, ¡debe ignorarse!
]

# TODO: Define la función 'actualizar_inventario' con los dos parámetros requeridos.
def actualizar_producto(productos_a_actualizar, inventario_ropa):
    for producto, nueva_cantidad in productos_a_actualizar:
        if producto in inventario_ropa:
            inventario_ropa[producto] = nueva_cantidad
        else: 
            print("el producto no existe, por lo que no se puede actualizar")
    return inventario_ropa

productos_actualizados = actualizar_producto(productos_a_actualizar, inventario_ropa)
# TODO: La función debe iterar sobre la lista de 'actualizaciones'.
# TODO: Dentro del bucle, comprueba SI el producto de la actualización EXISTE como clave en el 'inventario'.
# TODO: Si existe, actualiza su cantidad en el 'inventario'. Si no existe, no hagas nada.
# TODO: Llama a la función con los datos de ejemplo y luego imprime 'inventario_ropa'.
print(productos_actualizados)
# Resultado esperado: {"Calcetines": 60, "Gorra": 15, "Bufanda": 20}