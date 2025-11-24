# p062-conversion-temperaturas-v2.py
# El usuario debe introducir una temperatura inicial y una final en grados Celsius. El programa mostrará la conversión a grados Fahrenheit para cada grado en ese rango, incrementando de uno en uno.

print('\033[H\033[J')

while True:
    inicio = int(input("Introduce la temperatura inicial en °C: "))
    fin = int(input("Introduce la temperatura final en °C: "))

    print("--------------------")

    grado = inicio

    while grado <= fin:
        far = grado * 9/5 + 32
        print(grado, "°C =", f"{far:.1f}°F")
        grado += 1

    seguir = input("¿Desea continuar (S/N)? ").upper()
    if seguir == "N":
        break

print("Programa finalizado.")
