inventario_de_frutas = {"Manzana": 50, "Banana": 100}

# TODO: Define y prueba la función 'agregar_producto'.
def agregar_producto(fruta, cantidad, inventario_de_frutas):
    inventario_de_frutas[fruta] = cantidad
    return inventario_de_frutas
# TODO: Usa la función para agregar "Naranja" con una cantidad de 75.
agregar_producto("naranja", 75, inventario_de_frutas)
# TODO: Usa la función para agregar "Manzana" (que ya existe) con una cantidad de 40.
agregar_producto("manzana", 40, inventario_de_frutas)
# TODO: Muestra el inventario final y comprueba que Manzana tenga 40 unidades.
print(inventario_de_frutas)