claves = ["nombre", "edad", "ciudad"]
valores = ["Alice", 30, "New York"]

def listas_a_diccionario(claves, valores):
    diccionario_resultado = {}
    for clave, valores in zip(claves, valores):
        diccionario_resultado[claves] = valores
    # TODO: Itera sobre ambas listas al mismo tiempo (pista: usa zip())
    # TODO: Para cada par clave/valor, añádelo al diccionario_resultado
    return diccionario_resultado

perfil = listas_a_diccionario(claves, valores)
print(f"Diccionario final: {perfil}")