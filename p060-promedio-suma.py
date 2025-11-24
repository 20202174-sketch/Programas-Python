# p060-promedio-suma-v2.py
# Leer números introducidos por el usuario hasta que ingrese un 0. Al finalizar, mostrar el conteo total de números, la suma y el promedio de la serie.

print('\033[H\033[J')

while True:
    print("Introduce números (0 para terminar):")

    cantidad = 0
    suma = 0

    numero = 1  # Para entrar al ciclo

    while numero != 0:
        numero = int(input("> "))
        if numero != 0:
            cantidad += 1
            suma += numero

    print("--------------------")

    if cantidad > 0:
        promedio = suma / cantidad
        print("Se introdujeron", cantidad, "números.")
        print("La suma es:", suma)
        print("El promedio es:", promedio)
    else:
        print("No se introdujeron números válidos.")

    salir = input("¿Desea continuar (S/N)? ").upper()
    if salir == "N":
        break

print("Programa finalizado.")