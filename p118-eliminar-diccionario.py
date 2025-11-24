# p118-eliminar-diccionario.py
# Crea un diccionario municipios con los datos: Apozol: 1863, Calera: 1868, Fresnillo: 1554, Guadalupe:
# 1821, Jalpa: 1824, Jerez: 1824, Loreto: 1931, Mazapil: 1824, Momax: 1857.
# • Muestra el diccionario inicial.
# • Realiza las siguientes eliminaciones, mostrando el estado del diccionario después de cada operación:
# o Elimina Apozol (usando del).
# o Elimina Fresnillo (usando pop()).
# o Elimina el último elemento insertado (Momax) (usando popitem()).
# • Vacía el diccionario (usando clear()).
# • Muestra el diccionario final (vacío).

print('\033[H\033[J')
print("Manipulación de un diccionario de municipios\n")

municipios = {
    "Apozol": 1863,
    "Calera": 1868,
    "Fresnillo": 1554,
    "Guadalupe": 1821,
    "Jalpa": 1824,
    "Jerez": 1824,
    "Loreto": 1931,
    "Mazapil": 1824,
    "Momax": 1857
}

# -----------------------------------------
# Diccionario inicial
# -----------------------------------------
print("Diccionario inicial:")
print(municipios, "-", len(municipios), "\n")

# -----------------------------------------
# Eliminar usando del
# -----------------------------------------
del municipios["Apozol"]
print("Después de eliminar 'Apozol':")
print(municipios, "-", len(municipios), "\n")

# -----------------------------------------
# Eliminar usando pop()
# -----------------------------------------
municipios.pop("Fresnillo")
print("Después de usar pop('Fresnillo'):")
print(municipios, "-", len(municipios), "\n")

# -----------------------------------------
# Eliminar último elemento insertado usando popitem()
# -----------------------------------------
municipios.popitem()
print("Después de ejecutar popitem():")
print(municipios, "-", len(municipios), "\n")

# -----------------------------------------
# Vaciar diccionario
# -----------------------------------------
municipios.clear()
print("Diccionario tras aplicar clear():")
print(municipios, "-", len(municipios))
