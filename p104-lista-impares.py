# p104-lista-impares.py
# Leer un entero n. Llenar una lista con los primeros n números impares.
# Calcular e imprimir:
# • La suma y el promedio de los números.
# • Los números que son divisibles entre 3 y su suma.
# • Pedir un elemento a buscar en la lista original e indicar si está y en qué posición (índice).

print('\033[H\033[J')  # Limpiar pantalla

# -----------------------------------------
# ENTRADA
# -----------------------------------------
n = int(input("Introduzca la cantidad de números impares (n): "))

print("\n--- Generación de Lista ---")

imp = []   # lista de impares

# -----------------------------------------
# LLENADO DE LA LISTA
# -----------------------------------------
for k in range(n):
    imp.append(2 * k + 1)

print(f"Lista de los primeros {n} números impares:", imp)

# -----------------------------------------
# SUMA Y PROMEDIO
# -----------------------------------------
print("\n--- Cálculos ---")

total = 0
for x in imp:
    total += x

prom = total / n

print("Suma de los números:", total)
print("Promedio de los números:", prom)

# -----------------------------------------
# DIVISIBLES ENTRE 3
# -----------------------------------------
print("\n--- Divisibles entre 3 ---")

div_tres = []
for x in imp:
    if x % 3 == 0:
        div_tres.append(x)

suma_div = 0
for x in div_tres:
    suma_div += x

print("Números divisibles entre 3:", div_tres)
print("Suma de los números divisibles entre 3:", suma_div)

# -----------------------------------------
# BÚSQUEDA
# -----------------------------------------
print("\n--- Búsqueda ---")

busca = int(input("Introduzca elemento a buscar: "))

if busca in imp:
    pos = imp.index(busca)
    print(f"Resultado: El elemento {busca} está en la lista en la posición (índice) {pos}.")
else:
    print(f"Resultado: El elemento {busca} NO está en la lista.")
