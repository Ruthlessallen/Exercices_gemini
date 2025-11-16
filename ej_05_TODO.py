def filtrar_palabras_largas(lista_palabras):
    resultado_filtrado = []
    for palabra in lista_palabras:
        if len(palabra) > 5:
            resultado_filtrado.append(palabra)
    # TODO: Itera sobre cada palabra en la lista_palabras
    # TODO: Comprueba si la longitud de la palabra (len()) es mayor que 5
    # TODO: Si es más larga que 5, añádela a la lista resultado_filtrado
    return resultado_filtrado

palabras = ["gato", "perro", "elefante", "pez", "jirafa"]
largas = filtrar_palabras_largas(palabras)
print(f"Palabras largas: {largas}")

#def filtrar_palabras_largas_compacto(lista_palabras):
    # Esto hace exactamente lo mismo que tu bucle for
    #return [palabra for palabra in lista_palabras if len(palabra) > 5]

#palabras = ["gato", "perro", "elefante", "pez", "jirafa"]
#largas = filtrar_palabras_largas_compacto(palabras)
#print(f"Palabras largas: {largas}")