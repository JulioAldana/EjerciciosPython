# Ejercicio 13: suma de positivos, se detiene con negativo
suma = 0
while True:
    x = float(input("Número (+ para sumar, - para detener): "))
    if x < 0:
        break
    suma += x
print("Suma:", suma)
