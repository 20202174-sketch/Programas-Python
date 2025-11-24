# p097-procesar-datos-sensores.py
# Simulación de recolección y procesamiento de datos de sensores

import random

print('\033[H\033[J')
print("Simulando la recolección de datos de dos sensores...")

MAX = 10
sensor_a = []
sensor_b = []
todo = []
for _ in range(MAX):
    sensor_a.append(random.randint(1, 100)) # Llena la lista del sensor A
    sensor_b.append(random.randint(1, 100)) # Llena la lista del sensor B

print("\n--- Reporte de lecturas de sensores---")
print(f"Sensor A: {sensor_a}")
print(f"Sensor B: {sensor_b}")

for i in range(MAX):
    sensor_a[i] = sensor_a[i] ** 2
    sensor_b[i] = sensor_b[i] ** 2

    todo.append(sensor_a[i] + sensor_b[i])

print("\n--- Datos Procesados ---")
print(f"Sensor A (Transformados): {sensor_a}")
print(f"Sensor B (Transformados): {sensor_b}")
print(f"Datos Combinados: {todo}")