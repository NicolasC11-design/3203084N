def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"

def main():
    try:
        peso = float(input("Ingresa tu peso en kg: "))
        altura = float(input("Ingresa tu altura en metros: "))
        
        imc = calcular_imc(peso, altura)
        clasificacion = clasificar_imc(imc)

        print(f"\nTu IMC es: {imc:.2f}")
        print(f"Clasificación: {clasificacion}")
    
    except ValueError:
        print("⚠️ Entrada inválida. Asegúrate de usar números.")

if __name__ == "__main__":
    main()