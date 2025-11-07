# p125-segundo-examen-parcial.py
"""
Programa de gestión de un inventario
Gabriel Rodriguez Sustaita
Matrícula: 20202174
Materia: Computación Aplicada
Examen: Segundo Parcial
"""

print('\033[H\033[J')
 
inventario = []  # Lista de productos (cada producto es un diccionario)

print("Ingresa los datos de los productos. Deja el NOMBRE vacío para terminar.\n")

while True:
    nombre = input("Nombre del producto: ").strip()
    if nombre == "":   # fin cuando el nombre se deja vacío
        break

    try:
        precio = float(input("Precio: "))
    except ValueError:
        print("Error: Debe ingresar un número válido para el precio.")
        continue

    categoria = input("Categoría: ").strip()
    proveedor = input("Proveedor: ").strip()

    try:
        stock = int(input("Stock: "))
    except ValueError:
        print("Error: Debe ingresar un número entero para el stock.")
        continue

    producto = {
        "nombre": nombre,
        "precio": precio,
        "categoria": categoria,
        "proveedor": proveedor,
        "stock": stock
    }
    inventario.append(producto)

print("\n=== Datos ===")
print(inventario)

print("\n=== Tabla de datos ===")
print(f"{'NOMBRE':20} {'PRECIO':>10} {'CATEGORIA':15} {'PROVEEDOR':15} {'STOCK':>10}")
print("-" * 75)
for p in inventario:
    print(f"{p['nombre']:20} {p['precio']:10.2f} {p['categoria']:15} {p['proveedor']:15} {p['stock']:10}")

print("\n=== Resumen ===")

total_productos = len(inventario)
print(f"Total de productos registrados: {total_productos}")

# Conteos por categoría y proveedor 
categorias = {}
proveedores = {}
for p in inventario:
    cat = p["categoria"].lower()
    prov = p["proveedor"].lower()
    categorias[cat] = categorias.get(cat, 0) + 1
    proveedores[prov] = proveedores.get(prov, 0) + 1

# Totales y promedios
stocks = [p["stock"] for p in inventario]
precios = [p["precio"] for p in inventario]

if total_productos > 0:
    suma_stock = sum(stocks)
    prom_stock = suma_stock / total_productos
    suma_precios = sum(precios)
    prom_precios = suma_precios / total_productos

    # Producto más caro y más barato 
    precio_max = max(precios)
    precio_min = min(precios)
    pos_max = precios.index(precio_max)
    pos_min = precios.index(precio_min)
    producto_mas_caro = inventario[pos_max]
    producto_mas_barato = inventario[pos_min]
else:
    suma_stock = 0
    prom_stock = 0
    suma_precios = 0
    prom_precios = 0

print("\nProductos por categoría:")
if categorias:
    for cat, cnt in sorted(categorias.items()):
        print(f"{cat}: {cnt}")
else:
    print("(sin datos)")

print("\nProductos por proveedor:")
if proveedores:
    for prov, cnt in sorted(proveedores.items()):
        print(f"{prov}: {cnt}")
else:
    print("(sin datos)")

print(f"\nSuma total del stock: {suma_stock}")
print(f"Promedio de stock: {prom_stock:.2f}")
print(f"Suma total de precios: ${suma_precios:.2f}")
print(f"Promedio de precios: ${prom_precios:.2f}")

if total_productos > 0:
    print(f"\nEl producto más caro es '{producto_mas_caro['nombre']}' con un precio de ${precio_max:.2f}.")
    print(f"El producto más barato es '{producto_mas_barato['nombre']}' con un precio de ${precio_min:.2f}.")
else:
    print("\nNo hay productos para determinar el más caro o el más barato.")


