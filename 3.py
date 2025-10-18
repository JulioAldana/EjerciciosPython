# Ejercicio 3: mayor de tres números
a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))
mayor = a
if b > mayor:
    mayor = b
if c > mayor:
    mayor = c
print("Mayor:", mayor)
