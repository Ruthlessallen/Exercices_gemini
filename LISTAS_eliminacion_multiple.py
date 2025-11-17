"""
Crea la lista letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'].

Usa la palabra clave del con slicing para eliminar los elementos desde el índice 2 ('c') hasta el índice 5 ('f'), sin incluir 'g'.

Imprime el estado final de la lista letras.
"""
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
del letras[2:6]
print(letras)