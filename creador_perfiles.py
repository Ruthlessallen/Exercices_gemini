perfiles = {
"ruth":(56, "españa"),
"pepe":(42, "peru"),
"leon":(24, "italia"),
}
"""
for i in range(3):
    nombre = input("Escribe el nombre: ")
    edad = int(input("Escribe la edad: "))
    pais = input("Escribe el pais: ")

"""
print(perfiles)

pregunta_clave = input("escribe un nombre para saber su edad y pais: ")
if pregunta_clave in perfiles: 
    info = perfiles[pregunta_clave]
    print(f"edad {info[0]}, pais {info[1]}")
else: 
    perfiles[pregunta_clave] = ("pendiente", "desconocido")

print(perfiles)