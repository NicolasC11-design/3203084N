def calculadora():
    print("=== CALCULADORA SIMPLE ===")
    
    try:
        
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

    
        print("\nOperaciones disponibles:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")

        opcion = int(input("Seleccione una operación (1-4): "))

       
        if opcion == 1:
            resultado = num1 + num2
            operacion = "suma"
        elif opcion == 2:
            resultado = num1 - num2
            operacion = "resta"
        elif opcion == 3:
            resultado = num1 * num2
            operacion = "multiplicación"
        elif opcion == 4:
            if num2 == 0:
                raise ZeroDivisionError("❌ No se puede dividir por cero.")
            resultado = num1 / num2
            operacion = "división"
        else:
            raise ValueError("⚠️ Opción no válida.")

      
        print(f"\nEl resultado de la {operacion} es: {resultado:.2f}")

    except ValueError:
        print("⚠️ Error: Ingrese números válidos u opción correcta.")
    except ZeroDivisionError as e:
        print(f"⚠️ Error: {e}")


calculadora()