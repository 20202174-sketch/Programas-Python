# p064-verificar-palindromo-v2.py
# Solicitar al usuario que ingrese un número entero y determinar si es un palíndromo. Un número es palíndromo si se 121lee igual de izquierda a derecha que de derecha a izquierda (ej. 121, 3443).

print('\033[H\033[J')

while True:
    numero = input("Introduce un número para verificar si es palíndromo: ")

    invertido = ""
    indice = 0

    # Construir el número invertido recorriendo carácter por carácter
    while indice < len(numero):
        invertido = numero[indice] + invertido
        indice += 1

    # Comparar original vs invertido
    if numero == invertido:
        print("El número", numero, "es un palíndromo.")
    else:
        print("El número", numero, "no es un palíndromo.")

    if input("\n¿Desea continuar (S/N)? ").upper() == "N":
        break

print("Programa finalizado.")
