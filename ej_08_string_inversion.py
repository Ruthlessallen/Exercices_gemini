palabra = input("escribe una palabra: ").lower().replace(" ", "")
palabra_invertida = palabra[::-1]
if palabra != palabra_invertida:
    print("no es palindromo")
else:
    print("es palindromo")