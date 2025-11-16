lista_tareas = ["Comprar", "Estudiar"]

def completar_ultima_tarea(lista_tareas):
    if not lista_tareas:
        print("Se termino")
    tarea_completada = lista_tareas.pop() 
    print(f"Tarea '{tarea_completada}' completada.")
    if not lista_tareas:
        print("Se termino")


completar_ultima_tarea(lista_tareas)
completar_ultima_tarea(lista_tareas)
 