# p120-contar-caracteres.py
# Contar cuántas veces aparece cada carácter en una cadena

print('\033[H\033[J')
print("Frecuencia de caracteres en un texto\n")

texto = input("Ingrese una cadena: ")

# Diccionario vacío para almacenar caracteres
contar = {}

# Recorrer cada carácter
for ch in texto:
    if ch in contar:
        contar[ch] += 1
    else:
        contar[ch] = 1

# Mostrar resultado
print("\nResultado:")
print(contar)
