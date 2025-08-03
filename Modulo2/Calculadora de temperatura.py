def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_a_kelvin(c):
    return c + 273.15

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_a_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_a_celsius(k):
    return k - 273.15

def kelvin_a_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

try:
    
    print("=== Conversor de Temperaturas ===")
    print("1. Celsius a Fahrenheit y Kelvin")
    print("2. Fahrenheit a Celsius y Kelvin")
    print("3. Kelvin a Celsius y Fahrenheit")

    opcion = input("Seleccione una opción (1/2/3): ")

    
    if opcion == "1":
        c = float(input("Ingrese temperatura en °C: "))
        f = celsius_a_fahrenheit(c)
        k = celsius_a_kelvin(c)
        print(f"\n{c:.2f}°C = {f:.2f}°F = {k:.2f}K")

    elif opcion == "2":
        f = float(input("Ingrese temperatura en °F: "))
        c = fahrenheit_a_celsius(f)
        k = fahrenheit_a_kelvin(f)
        print(f"\n{f:.2f}°F = {c:.2f}°C = {k:.2f}K")

    elif opcion == "3":
        k = float(input("Ingrese temperatura en K: "))
        c = kelvin_a_celsius(k)
        f = kelvin_a_fahrenheit(k)
        print(f"\n{k:.2f}K = {c:.2f}°C = {f:.2f}°F")

    else:
        print("⚠️ Opción no válida. Por favor elija 1, 2 o 3.")

except ValueError:
    print("⚠️ Error: Ingrese un valor numérico válido.")