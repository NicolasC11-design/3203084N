print("Categoría de un estudiante según su edad ejercicio 2")
edad = int(input("Introduce la edad del estudiante: "))
if edad < 12:
    print("El estudiante es un niño.")
elif 12 <= edad < 18:
    print("El estudiante es un adolescente.")
else:
    print("El estudiante es un adulto.")