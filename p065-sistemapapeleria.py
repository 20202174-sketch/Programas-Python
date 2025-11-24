"""
p065-sistemapapeleria.py
Sistema de ventas para una papelería.
Autor: [Gabriel Rodriguez Sustaita]
Objetivo:
    Registrar ventas de copias por tipo, aplicar descuentos por volumen,
    generar un resumen detallado y clasificar el desempeño diario.
"""

print('\033[H\033[J')   # Limpiar pantalla

print("-----------------------------------------")
print("Papelería la UAZ, SA. de CV.\nSistema de ventas de copias")
print("-----------------------------------------")

num_ventas = 0

# Cantidades por tipo
cant_c = cant_o = cant_d = cant_p = 0

# Subtotales por tipo
tot_c = tot_o = tot_d = tot_p = 0

# -----------------------------------------
# Bucle principal de registro de ventas
# -----------------------------------------

while True:
    num_ventas += 1
    print(f"\nVenta {num_ventas}")

    # -----------------------------------------
    # Entrada: tipo de copia
    # -----------------------------------------
    tipo = input("Tipo de copia (C)arta $3, (O)ficio $4, (D)oble $6, (P)lano $12 ? ").upper()

    if tipo not in ("C", "O", "D", "P"):
        input(">>> Error: tipo inválido. Presiona <Enter> para continuar.")
        num_ventas -= 1
        continue

    # -----------------------------------------
    # Entrada: cantidad
    # -----------------------------------------
    cantidad = int(input("Cantidad ? "))

    # -----------------------------------------
    # Proceso: aplicar descuento por volumen
    # -----------------------------------------
    factor_desc = 1.0
    if cantidad > 50:
        factor_desc = 0.90
        print("*** Descuento del 10% aplicado por volumen! ***")

    # -----------------------------------------
    # Cálculo del subtotal según el tipo
    # -----------------------------------------
    if tipo == "C":
        subtotal = (cantidad * 3) * factor_desc
        cant_c += cantidad
        tot_c += subtotal

    elif tipo == "O":
        subtotal = (cantidad * 4) * factor_desc
        cant_o += cantidad
        tot_o += subtotal

    elif tipo == "D":
        subtotal = (cantidad * 6) * factor_desc
        cant_d += cantidad
        tot_d += subtotal

    elif tipo == "P":
        subtotal = (cantidad * 12) * factor_desc
        cant_p += cantidad
        tot_p += subtotal

    # -----------------------------------------
    # Continuar o finalizar registro
    # -----------------------------------------
    if input("¿Otra venta? (S/N) ").upper() != "S":
        break

# -----------------------------------------
# Cálculos finales
# -----------------------------------------
total_copias = cant_c + cant_o + cant_d + cant_p
total_general = tot_c + tot_o + tot_d + tot_p

# -----------------------------------------
# Sección de salida: resumen del día
# -----------------------------------------

print("\n---------------------------------------")
print("Resumen diario de ventas")
print("---------------------------------------")
print(f"Ventas realizadas: {num_ventas}")
print("-------------------------")
print(f"Carta      : {cant_c:3d}  -  $ {tot_c:8.2f}")
print(f"Oficio     : {cant_o:3d}  -  $ {tot_o:8.2f}")
print(f"Doble Of.  : {cant_d:3d}  -  $ {tot_d:8.2f}")
print(f"Plano      : {cant_p:3d}  -  $ {tot_p:8.2f}")
print("-------------------------")
print(f"Tot. Ventas: {total_copias:3d}  -  $ {total_general:8.2f}")

# -----------------------------------------
# Clasificación del desempeño
# -----------------------------------------
if total_general > 150:
    mensaje = "Venta superada"
elif total_general >= 50:
    mensaje = "Venta frecuente"
else:
    mensaje = "Venta moderada"

print(f"Esta venta es una : {mensaje}")
print("\nFin de ventas por hoy.")
