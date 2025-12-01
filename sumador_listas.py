def sumar_listas(lista_numeros): #def: define funcion llamada sumar_listas la cual tiene como parametro una lista
    
    #metodo A: usar for
    suma_a = 0 #un contador que se va sumando
    for i in lista_numeros: #itera sobre la lista de numeros
        suma_a += i #se suma al contador cada numero que se itera sobre la lista de numeros 
        

    #metodo B: usar while
    suma_b = 0 #contador, como en suma_a
    indice = 0 #un indice para poder limitar a la cantidad de numeros que hay en la lista
    while indice < len(lista_numeros): #mientras que el indice sea menor a la longitud(cantidad) de numeros que hay en la lista...
        numero = lista_numeros[indice] #numero es = al indice (el primer indice seria 0, o sea el primer elemento) de la lista
        suma_b += numero #se suma el numero de cada orden del indice al contador
        indice += 1 #se suma 1 al indice hasta que sea igual a la cantidad de la lista (y entonces se para el bucle)
        
    
    return suma_a, suma_b #retorna los datos que nos interesan, que son ambas sumas 

lista = [2, 5, 6, 8, 7, 2] #lista en cuestion

print(sumar_listas(lista)) #printea la funcion con el parametro de la lista