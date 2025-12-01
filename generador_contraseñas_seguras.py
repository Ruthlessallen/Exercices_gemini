import random

letras_min = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z'.split(',')
letras_may = [letras.upper() for letras in letras_min]
numeros = '0,1,2,3,4,5,6,7,8,9'.split(',')
simbolos = '!,@,#,$,%,^,&,-,_,,,<,>,/,*,+,-,='.split(',')
total_caracteres = letras_may + letras_min + numeros + simbolos

def generar_contraseña(longitud):
    caracteres = [
    random.choice(letras_min),
    random.choice(letras_may),
    random.choice(numeros),
    random.choice(simbolos) 
    ]
    contraseña = caracteres
    caracteres_faltantes = longitud - len(contraseña)
    for _ in range(caracteres_faltantes):
        caracter_aleatorio = random.choice(total_caracteres)
        contraseña.append(caracter_aleatorio)
    
    random.shuffle(contraseña)
    return "".join(contraseña)


contraseña_8 = generar_contraseña(8)
print(contraseña_8)
