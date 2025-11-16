inventario_libros = {"Matemáticas": 10, "Física": 12, "Química": 8, "Historia": 5}
actualizaciones_libros = [
    ("Física", 7),
    ("Biología", 20), # Ignorar
    ("Química", 10)
]

# TODO: Define y prueba la función 'actualizar_inventario' con estos datos.
def actualizar_libros(actualizaciones_libros,inventario_libros):
    for libro, cantidad in actualizaciones_libros:
        if libro in inventario_libros:
            inventario_libros[libro] = cantidad
        else: 
            print("ese libro no esta")
# TODO: Asegúrate de que el producto "Biología" NO se agregue al inventario.
    return inventario_libros
# Resultado esperado: {"Matemáticas": 10, "Física": 7, "Química": 10, "Historia": 5}
libreria_actualizada= actualizar_libros(actualizaciones_libros,inventario_libros)
print(libreria_actualizada)