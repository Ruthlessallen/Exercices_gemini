ciudades = ["Madrid", "París", "Roma", "Berlín", "Londres", "París"]

# TODO: Usa el método .index() para encontrar el índice de la PRIMERA aparición de "París" y guárdalo en 'indice_paris_1'.
indice_paris_1 = ciudades.index("París")
# TODO: Usa el método .index() para encontrar el índice de "Londres" y guárdalo en 'indice_londres'.
indice_londres = ciudades.index("Londres")
# TODO: Intenta usar .index() para buscar "Tokio" (¡causará un error!) y envuelve la llamada en un bloque try...except. Si ocurre el error, asigna el valor -1 a 'indice_tokio'.
try:
    indice_tokio = ciudades.index("tokio")
except:
    indice_tokio = -1
# TODO: Imprime 'indice_paris_1', 'indice_londres' e 'indice_tokio'.
print({indice_paris_1},{indice_londres},{indice_tokio})