lista = ["desarollo", "ordenador", "web", "API"]

lista.append("python")
print(f"Se ha añadido a la lista. {lista}")

t_lista = tuple(lista)

t_lista.append("key")#no se ejecuta jamas 

print(f"No se puede añadir porque es una tupla: {t_lista}")
