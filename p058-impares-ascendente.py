# p058-impares-ascendente.py
# Imprimir los números impares y su suma total en un rango ascendente desde 1 hasta un número n que elija el usuario.

print('\033[H\033[J')

while True:
    n = int(input("Ingresa un número límite: "))

    i = 1
    suma = 0

    while i <= n:
        if i % 2 != 0:  # Si es impar
            print(i)
            suma += i
        else:
            suma = suma
        i += 1

    print("La suma total de los impares es:", suma)

    if input('\n¿Deseas continuar (S/N)? ').upper() == 'N':
        break

print("Programa finalizado.")






