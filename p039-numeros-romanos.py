# p039-numeros-romanos
# pida al usuario un número entero entre 1 y 10 y muestre su equivalente en
# números romanos. Si el número está fuera de este rango, debe mostrar un mensaje de error.

print("\033[2J\033[H")
n1 = int(input("Entrada: "))

if n1 >= 1 and n1 <= 10:
    if n1 == 1:
        print("Salida: I")
    elif n1 == 2:
        print("Salida: II")
    elif n1 == 3:
        print("Salida: III")
    elif n1 == 4:
        print("Salida: IV")
    elif n1 == 5:
        print("Salida: V")
    elif n1 == 6:
        print("Salida: VI")
    elif n1 == 7:
        print("Salida: VII")
    elif n1 == 8:
        print("Salida: VIII")
    elif n1 == 9:
        print("Salida: IX")
    elif n1 == 10:
        print("Salida: X")
else:
     print(f"\033[31m\nSalida: Error: Numero invalido \033[0m")
