# p100-listas-multiplica.py
# Leer dos listas, cada una con 5 elementos numéricos. Crear una tercera lista multiplicando los elementos de las
# dos listas correspondientes. Imprimir las tres listas.

print('\033[H\033[J')  # Limpiar pantalla

# -----------------------------------
# LECTURA DE LISTA A (en una sola línea)
# -----------------------------------
A = []
print("Introduzca 5 números para la Lista A:", end=" ")

entrada = input()          # Ej: "2 4 6 8 10"
valores = entrada.split()  # Separa por espacios

# Convertir cada valor a entero
for v in valores:
    A.append(int(v))

# Validar que sean exactamente 5 elementos
while len(A) != 5:
    print("Debe introducir exactamente 5 números. Intente de nuevo:")
    A = []
    entrada = input()
    valores = entrada.split()
    for v in valores:
        A.append(int(v))

# -----------------------------------
# LECTURA DE LISTA B (en una sola línea)
# -----------------------------------
B = []
print("\nIntroduzca 5 números para la Lista B:", end=" ")

entrada = input()    
valores = entrada.split()

for v in valores:
    B.append(int(v))

while len(B) != 5:
    print("Debe introducir exactamente 5 números. Intente de nuevo:")
    B = []
    entrada = input()
    valores = entrada.split()
    for v in valores:
        B.append(int(v))

# -----------------------------------
# LISTA C (A * B)
# -----------------------------------
C = []
for i in range(5):
    C.append(A[i] * B[i])

# -----------------------------------
# RESULTADOS
# -----------------------------------
print("\n--- Resultados ---")
print("Lista A:", A)
print("Lista B:", B)
print("Lista C (A * B):", C)
