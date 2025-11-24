#p082-compara-rendimiento-inversion.py
# Desarrolla un programa que compare el crecimiento de dos fondos de inversión a lo largo de varios años. El usuario
# debe ingresar el monto inicial y la tasa de interés anual (porcentaje) para cada uno de los dos fondos, así como
# el número de años a proyectar. El programa deberá mostrar una tabla comparativa anual y al final indicar qué fondo
# generó un mayor rendimiento.

print('\033[H\033[J')   # Limpiar pantalla

# ------------------------------
# ENTRADA DE DATOS DEL FONDO A
# ------------------------------
print("\n--- Fondo de Inversión A ---")
iniA = float(input("Monto inicial: "))
tasaA = float(input("Tasa de interés anual (%): "))

# ------------------------------
# ENTRADA DE DATOS DEL FONDO B
# ------------------------------
print("\n--- Fondo de Inversión B ---")
iniB = float(input("Monto inicial: "))
tasaB = float(input("Tasa de interés anual (%): "))

# ------------------------------
# AÑOS A PROYECTAR
# ------------------------------
anios = int(input("\nAños a proyectar: "))

# ------------------------------
# PREPARAR VALORES INICIALES
# ------------------------------
valA = iniA
valB = iniB

print("\n--- Comparación de Rendimientos Anuales ---")
print("Año |   Fondo A   |   Fondo B")
print("-------------------------------------------")

# ------------------------------
# PROCESO: CÁLCULO AÑO POR AÑO
# ------------------------------
for ano in range(1, anios + 1):

    # Fórmulas de crecimiento anual
    valA = valA + (valA * tasaA / 100)
    valB = valB + (valB * tasaB / 100)

    # Salida formateada por año
    print(f"{ano:3d} |  $ {valA:8.2f} |  $ {valB:8.2f}")

# ------------------------------
# RESULTADO FINAL
# ------------------------------
print("\nResultado final:")

if valA > valB:
    print(f"El Fondo A (${valA:.2f}) superó al Fondo B (${valB:.2f}).")
elif valB > valA:
    print(f"El Fondo B (${valB:.2f}) superó al Fondo A (${valA:.2f}).")
else:
    print(f"Ambos fondos terminaron igual: ${valA:.2f}.")
