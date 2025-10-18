# Ejercicio 14: Fibonacci hasta N
N = int(input("Límite N: "))
a, b = 0, 1
while a <= N:
    print(a, end=" ")
    a, b = b, a + b
print()