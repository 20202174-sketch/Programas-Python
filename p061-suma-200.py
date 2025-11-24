# p061-suma-200-v2.py
# Leer números y sumarlos hasta que el total acumulado sea mayor o igual a 200. Al terminar, mostrar cuántos números se introdujeron y la suma final.

print('\033[H\033[J')

while True:
    total = 0
    cantidad = 0

    while total < 200:
        print("Suma actual:", total, end=". ")
        n = int(input("Introduce un número: "))
        total += n
        cantidad += 1

    print("--------------------")
    print("Meta de 200 alcanzada.")
    print("Suma final:", total)
    print("Total de números introducidos:", cantidad)

    opcion = input("¿Desea continuar (S/N)? ").upper()
    if opcion == "N":
        break

print("Programa finalizado.")
