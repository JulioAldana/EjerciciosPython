# Ejercicio 5: vocal o consonante
letra = input("Letra: ").lower()
if len(letra) != 1 or not letra.isalpha():
    print("Ingresa una sola letra válida")
elif letra in "aeiou":
    print("Vocal")
else:
    print("Consonante")