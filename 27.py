# Ejercicio 27: primeros 10 Fibonacci
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
print()