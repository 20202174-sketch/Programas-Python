#p003-area-triangulo.py
# calcula el area de un triangulo

print("Calculando el area de un triangulo")

print("Dame la base y la altura separados por un enter")

base, altura = int (input ()), int(input()) #lee dos valores

#proceso

area = base*altura /2 # la logica de algoritmos se evalua de izquierda a dercha

#salida
print("El triangulo de base", base)
print("El triangulo de altura", altura)
print("Tiene un area de ", area)

print(f"\nEl triangulo de base {base} y la altura {altura} tiene un area de {area:,.2f}")

print("El triangulo de base " + str(base) + "y altura" + str(altura) + "tiene un area de " + str(area))