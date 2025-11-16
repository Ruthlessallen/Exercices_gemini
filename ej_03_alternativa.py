capitales = {
    "España": "Madrid",
    "Francia": "París",
    "Italia": "Roma"
}
pais_buscado = input("¿De qué país quieres saber la capital?: ").capitalize() # Si escribes "francia"
capital = capitales.get(pais_buscado)
if capital is not None:
    print(f"La capital de {pais_buscado} es {capital}")
else:
    print("País no encontrado.")