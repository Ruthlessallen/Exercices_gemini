# Tienes este inventario inicial:
inventario_inicial = {"Laptop": 10, "Mouse": 25}

# TODO: Define la función 'agregar_producto' con los tres parámetros requeridos.
def agregar_producto(producto, cantidad, inventario_inicial):

# TODO: Dentro de la función, implementa la lógica para agregar o actualizar el 'nombre' con su 'cantidad' en el 'inventario'.
    inventario_inicial[producto] = cantidad
    return inventario_inicial

# TODO: Llama a la función para añadir "Teclado" con una cantidad de 15.
agregar_producto("Teclado", 15, inventario_inicial)
# TODO: Llama a la función para actualizar "Laptop" con una cantidad de 5 (debería resultar en 5, no 15).
agregar_producto("Laptop", 5, inventario_inicial)
# Resultado esperado después de las llamadas: {"Laptop": 5, "Mouse": 25, "Teclado": 15}
print(inventario_inicial)