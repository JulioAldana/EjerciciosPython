# Ejercicio 29: divisores de n
n = int(input("n: "))
print("Divisores:", end=" ")
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")
print()