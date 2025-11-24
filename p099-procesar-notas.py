# p099-procesar-notas.py
# Leer un número indeterminado de notas (calificaciones) entre 0 y 100, deteniéndose cuando el usuario introduzca
# un 0. Validar que todas las notas introducidas estén dentro del rango [0,100].

print('\033[H\033[J')   # Limpiar pantalla

# -----------------------------------------
# Variables acumuladoras
# -----------------------------------------
cadena_notas = ""      # Guardara todas las notas como texto: "85,92,78,"
cantidad = 0
suma = 0
mayor = -1
menor = 999

# -----------------------------------------
# LECTURA DE NOTAS
# -----------------------------------------
while True:
    nota = int(input("Introduzca nota (0 para detener): "))

    # Validación
    if nota < 0 or nota > 100:
        print("Entrada inválida, debe ser 0-100")
        continue

    if nota == 0:
        break

    # Acumular texto de notas
    cadena_notas += str(nota) + ","

    # Contadores y acumuladores
    cantidad += 1
    suma += nota

    # Máximo y mínimo
    if nota > mayor:
        mayor = nota
    if nota < menor:
        menor = nota

# -----------------------------------------
# SI NO SE INGRESARON NOTAS
# -----------------------------------------
if cantidad == 0:
    print("No se introdujeron notas.")
else:
    promedio = suma / cantidad

    print("\n--- Resultados ---")
    print("Total de notas introducidas:", cantidad)
    print("Lista de notas:", cadeia_notas := "[" + cadena_notas[:-1] + "]")  # Quitamos última coma

    print("Suma de notas:", suma)
    print("Promedio de notas:", promedio)
    print("Nota máxima:", mayor)
    print("Nota mínima:", menor)

    # -----------------------------------------
    # NOTAS MENORES AL PROMEDIO (sin listas)
    # -----------------------------------------
    print(f"Notas menores al promedio ({promedio}): ", end="")

    contador_menores = 0
    cadena_menores = "["

    # Para leer número por número desde la cadena
    numero = ""
    for ch in cadena_notas[:-1]:  # ignoramos última coma
        if ch != ",":
            numero += ch
        else:
            valor = int(numero)
            if valor < promedio:
                cadena_menores += str(valor) + ","
                contador_menores += 1
            numero = ""  # reiniciar número

    if contador_menores == 0:
        print("0")
        print("Lista de notas menores al promedio: []")
    else:
        print(contador_menores)
        print("Lista de notas menores al promedio:", cadena_menores[:-1] + "]")  # quitar coma final
