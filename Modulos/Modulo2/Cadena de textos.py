def analizar_texto():
    print("=== ANALIZADOR DE TEXTO ===")
    
    
    frase = input("Ingrese una frase: ")

   
    num_caracteres = len(frase)
    palabras = frase.split()
    num_palabras = len(palabras)

    
    mayusculas = frase.upper()
    minusculas = frase.lower()
    invertida = frase[::-1]

    
    buscar = input("\n¿Qué palabra desea buscar?: ").lower()
    ocurrencias = frase.lower().count(buscar)
    
    reemplazar = input(f"¿Por qué palabra desea reemplazar '{buscar}'?: ")
    nueva_frase = frase.replace(buscar, reemplazar)

    
    print("\n=== RESULTADOS ===")
    print(f"Caracteres: {num_caracteres}")
    print(f"Palabras: {num_palabras}")
    print(f"En mayúsculas: {mayusculas}")
    print(f"En minúsculas: {minusculas}")
    print(f"Al revés: {invertida}")
    print(f"Ocurrencias de '{buscar}': {ocurrencias}")
    print(f"Frase con reemplazo: {nueva_frase}")


analizar_texto()