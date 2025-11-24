# p077-triangulo-caracter.py
# Imprime un triángulo rectángulo de caracteres

print('\033[H\033[J')
print('Imprime un triangulo rectangulo de n renglones del caracter deseado')

n = int(input('¿Cuantos renglones tendra el triángulo? '))
car = input('¿Que caracter quieres usar? ')

# Bucle interior: controla las columnas (o caracteres por fila)
for i in range(1, n + 1):
    # El rango llega hasta 'i' para que cada fila tenga 'i' caracteres
    for j in range(i):
        # end evita el salto de línea para imprimir en la misma fila
        print(car, end='')
# genera el salto de línea para pasar a la siguiente fila
print()