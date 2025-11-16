inventario_almacen = {"Bolsa de Arroz": 50, "Aceite": 30}

def agregar_producto(nombre, cantidad, inventario_almacen):
    # TODO: Implementar la lógica para agregar/actualizar
    inventario_almacen[nombre] = cantidad
    pass

# TODO: Inicializa una variable de conteo (por ejemplo, 'i = 0').
contar_almacen = 0
# TODO: Crea un bucle 'while' que se ejecute 3 veces (mientras 'i < 3').
while contar_almacen < 3:
    # TODO: Pide al usuario el nombre del producto (input).
    producto = input("escribe un producto")
    # TODO: Pide al usuario la cantidad del producto (input, ¡recuerda convertirlo a entero!).
    cantidad = int(input("escribe la cantidad del producto"))
    # TODO: Llama a la función 'agregar_producto' con los valores obtenidos.
    agregar_producto(producto, cantidad, inventario_almacen)
    # TODO: Incrementa la variable de conteo.
    contar_almacen += 1

# TODO: Imprime el 'inventario_almacen' final.
print(inventario_almacen)