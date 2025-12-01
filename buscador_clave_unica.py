# Variables de prueba:
inventario = {"manzana": 10, "banana": 20, "naranja": 5}
claves = ["mango", "sandia", "naranja", "uva"]

def buscar_clave(inventario, claves):
    indice = 0
    while indice < len(claves):
        clave_actual = claves[indice]
        if clave_actual in inventario:
            return True
        indice += 1

    return False
print(buscar_clave(inventario, claves))