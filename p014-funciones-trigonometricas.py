# p014-funciones-trigonometricas
# Demostrar el uso de funciones trigonométricas básicas

import math

#Definir un Ángulo en grados y convertirlo a radianes
angulo = 45
radianes = math.radians(angulo)

#Calcular Funciones trigonometricas básicas
seno = math.sin(radianes)
coseno = math.cos(radianes)
tangente = math.tan(radianes)

#Convertir devuelta a grados para demostración
grados=math.degrees(radianes)

# Formatear la salida con f-strings para mejor presentación
salida = ('Resumen de funciones\n'
f'El seno es {seno:.4f}\n'
f'El coseno es {coseno:.4f}\n'
f'La tangente es {tangente:.4f}\n'
f'El angulo {angulo} grados, en radianes equivale a {radianes:.4f}\n'
f'Los {radianes:.4f} radianes equivalen a {grados:.1f}°\n')
# Mostrar la salida formateada
print(salida)