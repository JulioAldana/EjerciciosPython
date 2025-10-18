# Ejercicio 7: año de nacimiento válido
from datetime import date
anio = int(input("Año de nacimiento: "))
actual = date.today().year
if 1900 < anio < actual:
    print("Año válido")
else:
    print("Año NO válido")