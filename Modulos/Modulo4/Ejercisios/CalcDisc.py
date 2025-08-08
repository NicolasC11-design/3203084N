calc = {
    1: "Suma",
    2: "Resta",
    3: "Multiplicacion",
    4: "Division"
}
print("Calculadora")
print("Seleccione una opcion")
opcion = int(input("Seleccione una opcion"))
a = int(input("Ingrese el primer numero"))
b = int(input("Ingrese el Segundo numero"))


if opcion == 1:
       print(a+b)
elif opcion == 2:
        print(a-b)
elif opcion == 3:
        print(a*b)
elif opcion == 4:
        print(a/b)