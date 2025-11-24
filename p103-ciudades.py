# p103-ciudades.py
# Leer nombres de ciudades en una lista, continuando hasta que el usuario introduzca el carácter $. Imprimir:
# • Cuántos elementos tiene la lista.
# • La lista completa.
# • La lista ordenada en orden descendente.
# • Cuántas ciudades inician con una letra consonante y sus nombres.

print('\033[H\033[J')  # Limpiar pantalla

ciuds = []   # Lista para guardar ciudades

# -----------------------------------------
# LECTURA DE CIUDADES
# -----------------------------------------
while True:
    nombre = input("Introduzca nombre de ciudad ($ para detener): ")

    if nombre == "$":
        break

    ciuds.append(nombre)

# -----------------------------------------
# RESULTADOS INICIALES
# -----------------------------------------
print("\n--- Resultados ---")
print("Total de ciudades introducidas:", len(ciuds))
print("Lista original:", ciuds)

# -----------------------------------------
# ORDENAMIENTO DESCENDENTE (burbuja)
# -----------------------------------------
for i in range(len(ciuds) - 1):
    for j in range(len(ciuds) - 1 - i):
        if ciuds[j].lower() < ciuds[j + 1].lower():
            aux = ciuds[j]
            ciuds[j] = ciuds[j + 1]
            ciuds[j + 1] = aux

print("\nLista ordenada descendente:", ciuds)

# -----------------------------------------
# FILTRAR CIUDADES QUE INICIAN CON CONSONANTE
# -----------------------------------------
cons = []
letras_con = "bcdfghjklmnpqrstvwxyz"

for nom in ciuds:
    if nom[0].lower() in letras_con:
        cons.append(nom)

print("\nCiudades que inician con consonante:", len(cons))
print("Lista de ciudades con consonante inicial:", cons)
