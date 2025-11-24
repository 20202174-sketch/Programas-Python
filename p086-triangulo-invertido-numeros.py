# p086-triangulo-invertido-numeros.py
# Solicitar al usuario un número entero n que determinará la altura de un triángulo numérico invertido. El programa
# debe imprimir n renglones. El primer renglón contendrá los números de 1 a n, el segundo de 1 a n-1, y así sucesi-
# vamente hasta que el último renglón contenga solo el número 1.

print('\033[H\033[J')   # Limpiar pantalla

# ------------------------------
# ENTRADA DEL USUARIO
# ------------------------------
n = int(input("Dame un número: "))

print()  # Espacio visual

# ------------------------------
# TRIÁNGULO INVERTIDO
# ------------------------------
fila = n
while fila >= 1:

    num = 1
    while num <= fila:
        print(num, end=" ")
        num += 1

    print()
    fila -= 1
