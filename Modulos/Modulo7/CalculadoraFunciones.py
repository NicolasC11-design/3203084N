def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return a / b

OPERACIONES = {
    "1": ("Suma", sumar),
    "2": ("Resta", restar),
    "3": ("Multiplicación", multiplicar),
    "4": ("División", dividir),
}

def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("⚠️ Ingresa un número válido.")

def mostrar_menu():
    print("\n=== CALCULADORA ===")
    for clave, (nombre, _) in OPERACIONES.items():
        print(f"{clave}. {nombre}")
    print("0. Salir")

def calculadora():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "0":
            print("¡Hasta luego!")
            break

        if opcion not in OPERACIONES:
            print("⚠️ Opción no válida.")
            continue

        a = pedir_numero("Primer número: ")
        b = pedir_numero("Segundo número: ")

        nombre, funcion = OPERACIONES[opcion]

        try:
            resultado = funcion(a, b)
            print(f"Resultado ({nombre}): {resultado}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    calculadora()