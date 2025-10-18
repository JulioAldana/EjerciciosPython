# Ejercicio 6: primo o no primo
n = int(input("Entero >= 2: "))
es_primo = True
if n < 2:
    es_primo = False
else:
    i = 2
    while i * i <= n:
        if n % i == 0:
            es_primo = False
            break
        i += 1
print("Primo" if es_primo else "No primo")