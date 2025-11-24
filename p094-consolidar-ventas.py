# p094-consolidar-ventas.py
# Consolidar las ventas de dos sucursales, usando listas

print('\033[H\033[J')

print('Consolidar ventas de dos sucursales\n')
ventas = int(input('¿Cuántas ventas diarias se registrarán? '))

ventas1 = []
ventas2 = []
todo = []

print('\nRegistrando ventas de la Sucursal 1:')
for i in range(ventas):
    venta = int(input(f'Venta del día {i+1}: '))
    ventas1.append(venta)

print('\nRegistrando ventas de la Sucursal 2:')
for i in range(ventas):
    venta = int(input(f'Venta del día {i+1}: '))
    ventas2.append(venta)

for i in range(ventas):
    suma_dia = ventas1[i] + ventas2[i]
    todo.append(suma_dia)

print('\n--- Reporte de Ventas ---')
print(f'Sucursal 1: {ventas1}')
print(f'Sucursal 2: {ventas2}')
print(f'Ventas Consolidadas: {todo}')