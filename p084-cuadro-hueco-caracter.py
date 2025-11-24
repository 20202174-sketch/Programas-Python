# p084-cuadro-hueco-caracter.py
# El programa debe solicitar al usuario que ingrese el tamaño del lado de un cuadrado y el carácter con el que se
# dibujará. Luego, deberá imprimir en la consola un "cuadrado hueco", donde el carácter solo se utilice para dibujar
# el contorno del mismo.

print('\033[H\033[J')   # Limpiar pantalla

# ------------------------------
# ENTRADAS DEL USUARIO
# ------------------------------
lado = int(input("¿De qué tamaño será el lado del cuadrado? "))
car = input("¿Qué carácter quieres usar? ")

print()  # Espacio visual

# ------------------------------
# DIBUJAR EL CUADRADO HUECO
# ------------------------------
for f in range(1, lado + 1):
    for c in range(1, lado + 1):

        # Bordes del cuadrado
        if f == 1 or f == lado or c == 1 or c == lado:
            print(car, end=" ")
        else:
            print(" ", end=" ")

    print()  # Salto de línea por cada fila
