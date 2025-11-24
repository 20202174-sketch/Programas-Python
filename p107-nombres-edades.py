# p107-nombres-edades.py
# Gestion de nombres y edades usando diccionarios

print('\033[H\033[J')
print('Gestión de nombres y edades usando diccionarios\n')

datos = {}

print('Introduce nombres y edades (nombre vacio para terminar)')
while True:
    nombre = input('Dame el nombre: ')
    if nombre == '':break
    datos[nombre] = int(input('Edad ? '))
       
print(f'\nCenso de nombres y edades: \n{datos} - {len(datos)}\n')
print('\nListado y promedio de edades:')

s = 0
for n, e in datos.items():
    print(f'{n:<20} - {e:2}')
    s += e

print(f'\n\nLa suma es: {s} y el promedio: {s / len(datos):.2f}')
