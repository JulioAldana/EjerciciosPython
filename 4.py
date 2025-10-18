# Ejercicio 4: año bisiesto
anio = int(input("Año: "))
es_bisiesto = (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
print("Bisiesto" if es_bisiesto else "No bisiesto")
