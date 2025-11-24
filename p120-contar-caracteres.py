# p120-contar-caracteres.py
# Escribe un programa que pida al usuario que ingrese una cadena de texto.
# • Crea un diccionario vacío para almacenar la frecuencia (cantidad de apariciones) de cada carácter.
# • Itera sobre cada carácter en la cadena ingresada.
# • En cada iteración:
# o Si el carácter no existe como llave en el diccionario, agrégalo con un valor de 1.
# o Si el carácter ya existe, incrementa su valor actual en 1.
# • Al finalizar el ciclo, muestra el diccionario resultante con el conteo de caracteres.

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
