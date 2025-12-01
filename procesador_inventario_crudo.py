inventario = "Monitor:15|Teclado:40|Mouse:25|Webcam:10|Altavoz:25|Torre:200|Microfono:5".split("|")
listado_tuplas =[]
for p in inventario:
    pyp = p.split(":")
    nombre = pyp[0]
    cantidad = pyp[1]
    i_cant = int(cantidad)
    t_producto = (nombre, i_cant)
    listado_tuplas.append(t_producto)

print(listado_tuplas)