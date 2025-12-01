inventario = { #inventario vacio 

}
while True: #mientras que es true 
    usuario = input("Nombre articulo o fin") #variable con una entrada de datos string
    if usuario == "fin": #si el usuario escribe "fin"
        break #para el while
    precio = int(input("Precio del articulo")) #variable con entrada de datos int
    inventario[usuario] = precio #entrada al inventario [articulo] = precio
    for i in inventario.items(): #iteracion sobre los items (keys, values) de inventario
        print(i) #printea la iteracion: primero las keys, luego las values