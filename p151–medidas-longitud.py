# p151-medidas-longitud.py
# Desarrolla un programa que funcione como un conversor de unidades de longitud. El programa debe mostrar un
# menú y utilizar dos funciones separadas:
# 1. Una función para convertir pulgadas a centímetros (fórmula: $cm = pulgadas \times 2.54$).
# 2. Una función para convertir metros a pies (fórmula: $pies = metros \times 3.281$).
# El programa debe solicitar los datos al usuario según la opción elegida y mostrar el resultado.

def convertir_pulgadas_cm(valor: float) -> float:
    return valor * 2.54

def convertir_metros_pies(valor: float) -> float:
    return valor * 3.281

def ejecutar_menu() -> None:
    while True:
        print("\n*** Conversor de Medidas ***")
        print("1) Convertir pulgadas a centímetros")
        print("2) Convertir metros a pies")
        print("3) Salir del programa")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            pulg = float(input("Cantidad en pulgadas: "))
            cm = convertir_pulgadas_cm(pulg)
            print(f"{pulg} pulgadas equivalen a {cm} centímetros.")

        elif opcion == "2":
            mts = float(input("Cantidad en metros: "))
            pies = convertir_metros_pies(mts)
            print(f"{mts} metros equivalen a {pies} pies.")

        elif opcion == "3":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida, intenta nuevamente.")

if __name__ == "__main__":
    ejecutar_menu()
