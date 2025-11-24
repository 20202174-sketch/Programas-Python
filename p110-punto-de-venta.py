# p110-punto-de-venta.py
# Simulacion de un punto de venta usando diccionarios

print('\033[H\033[J')
print('Simulando un punto de venta...\n')
menu = {
    'taco': 18.50,
    'burrito': 45.00,
    'quesadilla': 35.00,
    'refresco': 20.00,
    'agua': 15.00
}
print('--- Bienvenido a "El Taco Feroz" ---')
print('Este es nuestro menú:')
for item, precio in menu.items():
    print(f' - {item:<12} : ${precio:,.2f}')

orden = {}
total_general = 0

while True:
    producto = input('\n¿Qué desea ordenar?').lower()
    if producto == 'fin':break
    cantidad = int(input('Cantidad'))
    orden[producto] = orden.get(producto,0) + cantidad
    print(f'Agregamos {cantidad} {producto} a tu orden ')

print(f'Tu orden fue:\n {orden}')

print('\n---RECIBO---')
if not orden:
    print('No compraste nada')
else:
    for producto, cantidad in orden.item():
        precio_unitario = menu[producto]
        subtotal = precio_unitario * cantidad
        print(f'{cantidad} x {producto:<12} : {subtotal:.2f}')
        total_general += subtotal

print("-" * 35)
print(f'Total a pagar: {total_general:,.2f}')
print('gracias por tu compra')

