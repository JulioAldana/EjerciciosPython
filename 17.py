# Ejercicio 17: media de N números
n = int(input("¿Cuántos números? "))
suma = 0
i = 0
while i < n:
    suma += float(input(f"Num {i+1}: "))
    i += 1
media = suma / n if n > 0 else 0
print("Media:", media)