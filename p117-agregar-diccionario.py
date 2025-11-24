# p117-agregar-diccionario.py
# Crea un diccionario llamado ventas con los siguientes datos: Juan: 1550, Jose: 2600, Maria: 2220.
# • Muestra el diccionario.
# • Agrega los siguientes vendedores y sus ventas al diccionario:
# o Rocio: 2500 (usando []).
# o Mateo: 1567 (usando []).
# o Andrea: 9567 (usando update()).
# o Miguel: 1234 (usando update()).
# • Muestra el diccionario actualizado.

print('\033[H\033[J')
print("Actualizando un diccionario de ventas\n")

ventas = {
    "Juan": 1550,
    "Jose": 2600,
    "Maria": 2220
}

# Mostrar diccionario original
print("Ventas iniciales:")
print(ventas, "-", len(ventas), "\n")

# Agregar elementos con []
ventas["Rocio"] = 2500
ventas["Mateo"] = 1567

# Agregar elementos con update()
ventas.update({"Andrea": 9567})
ventas.update({"Miguel": 1234})

# Mostrar diccionario actualizado
print("Ventas actualizadas:")
print(ventas, "-", len(ventas))
