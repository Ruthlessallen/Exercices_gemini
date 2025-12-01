lista = ['user_A@', 'user_B!', 'user_C!', 'user_D', 'user_E']
contador = 0

for i in lista: 
        if "@" in i or "!" in i:
            print(f"{i} INVALIDO")
            contador +=1            
        else: 
            print(f"{i} VALIDO")

        if contador >2:
            print("limite superado")
            break