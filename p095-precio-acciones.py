# p095-precio-acciones.py
# Análisis básico de protafoio de acciones
print('\033[H\033[J')

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
precios = [150.25, 152.50, 149.75, 155.00, 153.20]

precio_max = max(precios)
precio_min = min(precios)

pos_max = precios.index(precio_max)
pos_min = precios.index(precio_min)

print(f"Precios de la semana: {precios}")
print(f"El precio más alto fue ${precio_max} el día {dias[pos_max]}.")
print(f"El precio más bajo fue ${precio_min} el día {dias[pos_min]}.")