# p101-mes-dia-nombre.py
# Leer un número de mes (ej. 4). Guardar los días de cada mes en una lista y los nombres de los meses en otra
# lista. Asumir 28 días para febrero. Imprimir el nombre del mes y la cantidad de días del mes correspondiente (ej.
# marzo, 30).

print('\033[H\033[J')  # Limpiar pantalla

# Listas con los meses y sus días correspondientes
mes_nombre = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
              "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

mes_dias = [31, 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31]

# Leer el número de mes
num_mes = int(input("Introduzca un número de mes (1-12): "))

# Validar rango
if num_mes >= 1 and num_mes <= 12:
    print("\n--- Resultados ---")
    print("Mes:", mes_nombre[num_mes - 1])
    print("Días:", mes_dias[num_mes - 1])
else:
    print("Error: número fuera del rango permitido.")
