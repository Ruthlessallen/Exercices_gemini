diccionario = {
    "nombre" : "Ruth",
    "edad" : "28",
    "empleo" : "estudiante", 
    "altura" : "1,40cm",
    "peso" : "50kg"
}
usuario = input("elige el dato a buscar: Nombre, edad, empleo, altura o peso: ").lower()
datos = diccionario.get(usuario)
if datos is not None:
    print(f"Es {datos}")
else:
    print("no tengo esa info")

