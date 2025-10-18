# Ejercicio 25: primos del 1 al 50
def es_primo(x):
    if x < 2:
        return False
    d = 2
    while d*d <= x:
        if x % d == 0:
            return False
        d += 1
    return True

for i in range(1, 51):
    if es_primo(i):
        print(i, end=" ")
print()