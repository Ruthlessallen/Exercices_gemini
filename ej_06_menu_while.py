lista_tareas = ["ir a comprar"]
ejecucion = True
while ejecucion == True:
    print("MENU")
    print("1. Ver tareas")
    print("2. Añadir tareas")
    print("3. Completar tareas")
    print("4. Salir")
    opcion = input("ELIGE: ").lower()
    if opcion == "1":
        print("LISTA: ")
        if not lista_tareas:
            print("No hay nada en la lista de tareas")
        else: 
            for numero, tarea in enumerate(lista_tareas, 1):
                print(f"{numero}. {tarea}")
    elif opcion == "2":
        añadir_tarea = input("Elige la tarea a añadir: ").lower()
        lista_tareas.append(añadir_tarea)
    elif opcion == "3":
        for numero, tarea in enumerate(lista_tareas, 1):
                print(f"{numero}. {tarea}")
        eliminar_tarea = input("Elige la tarea completada: ").lower()
        lista_tareas.remove(eliminar_tarea)
    elif opcion == "4":
        ejecucion = False
if ejecucion == False:
    print("Saliendo del sistema de tareas.")
