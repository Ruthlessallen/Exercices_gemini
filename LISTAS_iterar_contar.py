precios = [12.50, 4.99, 25.00, 8.75, 4.99]

# TODO: Inicializa una variable llamada 'suma_total' a 0.
suma_total = 0
# TODO: Itera sobre la lista 'precios' y, en cada iteración, suma el precio actual a 'suma_total'.
for i in precios:
    suma_total += i
# TODO: Usa el método .count() para saber cuántas veces aparece el valor 4.99 y guárdalo en 'cantidad_ofertas'.
cantidad_ofertas = precios.count(4.99)

# TODO: Imprime 'suma_total' y 'cantidad_ofertas'.
print(suma_total)
print(cantidad_ofertas)