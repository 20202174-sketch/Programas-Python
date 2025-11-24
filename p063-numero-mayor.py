# p063-numero-mayor-v2.py
# Leer una serie de números hasta que el usuario ingrese un 0. Al terminar, el programa deberá mostrar cuál fue el número más grande de todos los introducidos.

print('\033[H\033[J')

while True:
    print("Introduce números (0 para terminar):")

    maximo = 0
    primero = True   # Indica si aún no se ha registrado un primer número

    while True:
        n = int(input("> "))

        if n == 0:
            break

        if primero:        # Primer número introducido
            maximo = n
            primero = False
        elif n > maximo:   # Se compara después del primero
            maximo = n

    print("--------------------")

    if not primero:
        print("El número mayor fue:", maximo)
    else:
        print("No se introdujeron números.")

    salir = input("¿Desea continuar (S/N)? ").upper()
    if salir == "N":
        break

print("Programa finalizado.")
