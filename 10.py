# Ejercicio 10: precio con descuento
precio = float(input("Precio: "))
porc = float(input("Descuento (%): "))
final = precio * (1 - porc / 100)
print("Precio final:", round(final, 2))