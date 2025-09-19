#p018-area-volumen-cilindro
#calcula el área y volumen de un cilindro.

print("="*142)
print("Este programa calcula el area y volumen de un cilindro, \033[91m\nEs imporante que todos los datos que ingreses esten en la misma unidad de medida, y en la salida el numero mostrado sera de la misma unidad de medida \033[0m ")
print("="*142)

import math #se importa la libreria de matemaicas para el pi

#Se solicita el radio y la altura del cilindro al usuario
radio = float(input("Ingresa el radio de tu cilindro: "))
altura = float(input("Ingresa el altura de tu cilindro"))

#Las formulas para el calculo del area y del volumen son las siguientes
area = math.pi * radio * (radio + altura)
volumen = math.pi * (radio**2) * altura

#Muestra el area y el volumen con solo dos decimales
print(f"El area de tu cilindro es: {area:.2f} y el volumen es: {volumen:.2f}")