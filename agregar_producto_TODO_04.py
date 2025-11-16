inventario_de_bebidas = {"Agua": 200, "Refresco": 150}

# TODO: Define y prueba la función 'agregar_producto'.
def agregar_producto(bebida, cantidad, inventario_de_bebidas):
    inventario_de_bebidas[bebida] = cantidad
    return inventario_de_bebidas

# TODO: Crea un bucle 'while True'.
while True:
    # TODO: Pide al usuario el nombre del producto.
    producto = input("Escribe el producto. Escribe Fin si quieres finalizar.  ").lower()
    # TODO: Usa una condición 'if' para romper el bucle si el nombre es "fin".
    if producto != "fin":
        cantidad = int(input("escribe la cantidad: "))
        agregar_producto(producto, cantidad, inventario_de_bebidas)
    elif producto == "fin":
        break
    # TODO: Si no es "fin", pide la cantidad y agrega el producto.

# TODO: Imprime el 'inventario_de_bebidas' final.
print(f"Tu inventario es: {inventario_de_bebidas}")