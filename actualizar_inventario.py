juguetes = {"Carro": 10, "Muñeca": 5, "Bloques": 25}
nuevos_datos = [("Muñeca", 1), ("Pelota", 50), ("Carro", 8)]

def actualizar(nuevos_datos, juguetes):
    for juguete, cantidad in nuevos_datos:
        if juguete in juguetes:
            juguetes[juguete] = cantidad
        else: 
            print(f"el juguete {juguete} no existe")
    return juguetes

listado_juguetes = actualizar(nuevos_datos, juguetes)

print(listado_juguetes)