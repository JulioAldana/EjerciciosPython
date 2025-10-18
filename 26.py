# Ejercicio 26: números triangulares (n términos)
n = int(input("Términos: "))
suma = 0
for k in range(1, n+1):
    suma += k
    print(suma, end=" ")
print()