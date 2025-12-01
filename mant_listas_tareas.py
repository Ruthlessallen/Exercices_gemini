tareas = [{
    'nombre': 'Python',
    'estado': 'pendiente'
    },
    {'nombre': 'Gym',
    'estado': 'completa'
    }, 
    {'nombre': 'Email',
    'estado': 'pendiente'
    }] 

for i in tareas:
    if i['estado'] == 'pendiente':
        i['estado'] = 'en_progreso' 
        
tarea_final = []
for f in tareas: 
    if f['nombre'] != 'Email':
        tarea_final.append(f)
    else:
        continue
print(tareas)
print(tarea_final)