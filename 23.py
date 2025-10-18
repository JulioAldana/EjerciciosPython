# Ejercicio 23: suma de pares hasta n
n = int(input("n: "))
suma = 0
for i in range(2, n+1, 2):
    suma += i
print("Suma de pares:", suma)