# p085-rombo-caracter.py
# Solicitar al usuario un número entero impar n que representará la altura y el ancho máximo de un rombo. El pro-
# grama deberá dibujar el rombo utilizando el carácter que el usuario elija.

print('\033[H\033[J')   # Limpiar pantalla

# ------------------------------
# ENTRADA VALIDADA
# ------------------------------
n = int(input("Dame un número impar para la altura: "))

while n % 2 == 0:
    print("Error: el número debe ser impar.")
    n = int(input("Dame un número impar para la altura: "))

car = input("¿Qué carácter quieres usar? ")

print()  # Espacio visual

# ------------------------------
# PARTE SUPERIOR DEL ROMBO
# ------------------------------
nivel = 1
while nivel <= n:
    espacios = (n - nivel) // 2
    print(" " * espacios + car * nivel)
    nivel += 2   # Solo valores impares

# ------------------------------
# PARTE INFERIOR DEL ROMBO
# ------------------------------
nivel = n - 2
while nivel >= 1:
    espacios = (n - nivel) // 2
    print(" " * espacios + car * nivel)
    nivel -= 2
