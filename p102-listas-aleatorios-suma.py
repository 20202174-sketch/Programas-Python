# p102-listas-aleatorios-suma.py
# Generar 2 listas de 10 números aleatorios cada una. Crear una tercera lista donde el elemento sea la suma de
# los correspondientes de las listas A y B, solo si AMBOS elementos son impares; de lo contrario, el elemento de
# la tercera lista será 0. Imprimir las 3 listas.

print('\033[H\033[J')  # Limpiar pantalla

import random

A = []
B = []
C = []

# ---------------------------------------
# Generar listas A y B con 10 aleatorios
# ---------------------------------------
for k in range(10):
    A.append(random.randint(1, 100))
    B.append(random.randint(1, 100))

# ---------------------------------------
# Crear lista C con la condición de impares
# ---------------------------------------
for k in range(10):
    if A[k] % 2 != 0 and B[k] % 2 != 0:
        C.append(A[k] + B[k])
    else:
        C.append(0)

# ---------------------------------------
# Impresión de resultados
# ---------------------------------------
print("--- Listas Generadas ---")
print("Lista A:", A)
print("Lista B:", B)

print("\n--- Resultados (suma solo si ambos son impares) ---")
print("Lista C:", C)
