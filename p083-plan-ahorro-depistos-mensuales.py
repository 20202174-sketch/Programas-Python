# p083-plan-ahorro-depositos-mensuales.py
# El programa simulará un plan de ahorro. Deberá solicitar al usuario un monto inicial, un depósito mensual fijo,
# una tasa de interés mensual (porcentaje), y el número total de meses del plan. El programa debe mostrar una
# tabla que detalle, para cada mes, el saldo inicial, el interés ganado en ese mes, y el saldo final. El interés se calcula
# sobre el saldo inicial antes de sumar el nuevo depósito.

print('\033[H\033[J')   # Limpiar pantalla

# ------------------------------
# ENTRADAS DEL USUARIO
# ------------------------------
ini = float(input("Monto inicial de ahorro: "))
dep = float(input("Depósito mensual: "))
tasa = float(input("Tasa de interés mensual (%): "))
meses = int(input("Número de meses a simular: "))

# ------------------------------
# PREPARAR SALDO INICIAL
# ------------------------------
saldo = ini

print("\n--- Plan de Ahorro Detallado ---")

# ------------------------------
# CÁLCULO MES A MES
# ------------------------------
for mes in range(1, meses + 1):

    # Interés calculado sobre el saldo inicial
    interes = saldo * tasa / 100

    # Saldo final después de aplicar interés y sumar depósito
    saldo_final = saldo + interes + dep

    # Mostrar resultados del mes
    print("Mes", mes, 
          ": Saldo Inicial: $", f"{saldo:7.2f}",
          " | Interés: $", f"{interes:6.2f}",
          " | Saldo Final: $", f"{saldo_final:7.2f}", sep='')

    # Actualizar saldo para siguiente mes
    saldo = saldo_final

# ------------------------------
# SALIDA FINAL
# ------------------------------
print(f"\nAl final de {meses} meses, tendrás ${saldo:.2f}")
