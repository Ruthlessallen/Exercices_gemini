def contar_letras_mixtas(texto):
    contador_vocales = 0
    consonantes_contador = 0
    vocal ="aeiuo"
    consonante = "qwrtypsdfghjklñmnbvxz"
    for caracter in texto:
        if caracter in vocal:
            contador_vocales += 1  
        elif caracter in consonante:
            consonantes_contador += 1
    return contador_vocales, consonantes_contador  

texto = input("escribe una palabra: ")
total_vocal, total_consonante = contar_letras_mixtas(texto)
print(f"la palabra {texto} tiene {total_vocal} vocales y {total_consonante} consonantes")

