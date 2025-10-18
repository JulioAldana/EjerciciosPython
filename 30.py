# Ejercicio 30: primeros 10 primos
def es_primo(x):
    if x < 2:
        return False
    d = 2
    while d*d <= x:
        if x % d == 0:
            return False
        d += 1
    return True

encontrados = 0
n = 2
while encontrados < 10:
    if es_primo(n):
        print(n, end=" ")
        encontrados += 1
    n += 1
print()