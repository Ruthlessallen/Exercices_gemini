db_usuarios = {

    }

def agregar_usuario(db_usuarios, nombre, rol):

    if nombre not in db_usuarios:
        db_usuarios[nombre] = rol
    elif nombre in db_usuarios and rol == "rol_super_admin":
        db_usuarios[nombre] = "rol_super_admin"
    else:
        pass

    return db_usuarios


p_nombre = input("Cual es el nombre: ")
p_rol = input("cual es el rol: ")
db_usuarios = agregar_usuario(db_usuarios, p_nombre, p_rol)

print(f"El diccionario es {db_usuarios}")