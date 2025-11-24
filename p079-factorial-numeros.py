# p079-factorial-numeros.py
# Calcula el factorial de n numeros
# Imprime el factorial de los números desde 1 hasta n

print('Calcula el factorial de 1 a n\n')
try:
    n = int(input('¿Hasta que numero deseas calcular el factorial? '))
    for i in range(1, n + 1):
        factorial = 1 # Reinicia el factorial para cada nuevo numero
        for j in range(1, i + 1):
            factorial *= j
        print(f'El factorial de {i}! es = {factorial}')
except ValueError:
    print('Error: Por favor, introduce un numero entero válido.')