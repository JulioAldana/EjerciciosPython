# Ejercicio 18: termina cuando entra 0
conteo = 0
while True:
    x = float(input("Número (0 para salir): "))
    if x == 0:
        break
    conteo += 1
print("Cantidad ingresada (sin contar el 0):", conteo)