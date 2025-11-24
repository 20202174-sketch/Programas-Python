# p059-pares-descendente.py
# Imprimir los números pares y su suma total en un rango descendente desde 100 hasta un número n que elija el usuario.

print('\033[H\033[J')

while True:
    n = int(input("Introduce un número límite (menor a 100): "))

    num = 100
    suma = 0
    primero = True

    print("Números pares:", end=" ")

    while num >= n:
        if num % 2 == 0:
            if primero:
                print(num, end="")
                primero = False
            else:
                print(", " + str(num), end="")

            suma += num
        num -= 1

    print("\nLa suma de los pares es:", suma)

    if input("¿Desea continuar (S/N)? ").upper() == "N":
        break

print("Programa finalizado.")
