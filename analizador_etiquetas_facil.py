texto = input("Escribe un texto para analizar separado por ','") #solo arroja str 
lista = texto.split(", ")
for p in lista: 
    print(f" El tipo de etiqueta de {p} es {type(p)}")
