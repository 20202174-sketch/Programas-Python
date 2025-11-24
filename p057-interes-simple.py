# p057-interes-simple.py
# Calcula los años necesarios para alcanzar una meta de ahorro con interés simple.

while True:
    print('\033[H\033[J')
    print("Calculadora de Años para Meta de Ahorro con interés simple")
    print("-" * 60)
    
    capital_inicial = float(input("Introduce el capital inicial: "))
    tasa_interes = float(input("Introduce la tasa de interés anual (%): "))
    meta_ahorro = float(input("Introduce la meta de ahorro: "))
    
    capital_actual = capital_inicial
    años = 0
    interes_anual_fijo = capital_inicial * (tasa_interes/ 100)

    while capital_actual <= meta_ahorro:
        capital_actual += interes_anual_fijo
        años += 1
    
    print("\n" + "-" * 60)
    print(f"Para alcanzar o superar tu meta de ${meta_ahorro:,.2f}, necesitarás {años} años.")
    print(f"El monto final acumulado será de ${capital_actual:,.2f}.")
    print("-" * 60)
    if input('\n¿Deseas realizar otro cálculo (S/N)? ').upper()== 'N':break

    print("\nFin del programa")