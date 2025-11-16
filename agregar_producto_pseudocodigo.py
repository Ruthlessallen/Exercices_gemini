""" EJERCICIO 3
def agregar_producto(inventario, producto, precio):
    inventario[producto] = precio
    return inventario
""" 
#EJERCICIO 5 CREAR INVENTARIO 

inventario_tienda = {

}
def agregar_producto(producto, precio, inventario):
    inventario[producto] = precio
    return inventario

agregar_producto("camiseta", 20, inventario_tienda)
agregar_producto("pantalon", 15, inventario_tienda)
agregar_producto("camiseta", 25, inventario_tienda)
print(inventario_tienda)