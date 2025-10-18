# Ejercicio 24: factorial
n = int(input("n (>=0): "))
fact = 1
for i in range(2, n+1):
    fact *= i
print(f"{n}! =", fact)