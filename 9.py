# Ejercicio 9: calificación en letras
n = int(input("Puntos (0-100): "))
if 90 <= n <= 100:
    letra = "A"
elif 80 <= n <= 89:
    letra = "B"
elif 70 <= n <= 79:
    letra = "C"
elif 60 <= n <= 69:
    letra = "D"
elif 0 <= n <= 59:
    letra = "F"
else:
    letra = "Fuera de rango"
print("Calificación:", letra)