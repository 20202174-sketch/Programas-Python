# p081-suma-potencias.py
# Suma las potencias de un número x desde x^1 hasta x^n

print('\033[H\033[J')
print('Suma de Potencias \n')

x = float(input('Introduce el valor de x: '))
n = int(input('Introduce el valor de (n): '))

suma_total = 0

termino_actual = 1
for j in range(n+1):
    suma_total += termino_actual
    print(f'Término {x}^{j} = {termino_actual}')
    termino_actual *= x

print(f'\nEl resultado de la serie es: {suma_total}')