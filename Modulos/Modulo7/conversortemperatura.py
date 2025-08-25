LIMITES = {"C": -273.15, "F": -459.67, "K": 0.0}

def validar(escala, valor):
    if valor < LIMITES[escala]:
        raise ValueError(f"⚠️ Por debajo del cero absoluto en {escala}")

def c_to_f(c): return (c * 9/5) + 32
def f_to_c(f): return (f - 32) * 5/9
def c_to_k(c): return c + 273.15
def k_to_c(k): return k - 273.15
def f_to_k(f): return c_to_k(f_to_c(f))
def k_to_f(k): return c_to_f(k_to_c(k))

OPCIONES = {
    "1": ("C", "F", c_to_f),
    "2": ("F", "C", f_to_c),
    "3": ("C", "K", c_to_k),
    "4": ("K", "C", k_to_c),
    "5": ("F", "K", f_to_k),
    "6": ("K", "F", k_to_f),
}

def mostrar_menu():
    print("\n=== CONVERSOR DE TEMPERATURA ===")
    print("1. Celsius -> Fahrenheit")
    print("2. Fahrenheit -> Celsius")
    print("3. Celsius -> Kelvin")
    print("4. Kelvin -> Celsius")
    print("5. Fahrenheit -> Kelvin")
    print("6. Kelvin -> Fahrenheit")
    print("0. Salir")

def pedir_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("⚠️ Ingresa un número válido.")

def conversor():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "0":
            print("Programa finalizado. 👋")
            break

        if opcion not in OPCIONES:
            print("⚠️ Opción no válida.")
            continue

        origen, destino, funcion = OPCIONES[opcion]
        valor = pedir_float(f"Ingresa el valor en {origen}: ")

        try:
            validar(origen, valor)
            resultado = funcion(valor)
            validar(destino, resultado)
            print(f"{valor:.2f}{origen} = {resultado:.2f}{destino}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    conversor()