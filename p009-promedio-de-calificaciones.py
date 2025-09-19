# p009-promedio-de-calificaciones
# Objetivo: Calcular el promedio de tres calificaciones ingresadas por el usuario.

print("Calculando el promedio de 3 calificaciones\n")


#Solicitar las calificaciones en una sola linea separadas por un espacio.

print("Dame 3 calificaciones separadas por un espacio:")

cal1,cal2,cal3=input().split()
cal1,cal2,cal3=int(cal1),int(cal2),int(cal3) #Es importante recordar que el resultado de input() siempre es una cadena de texto (string). en esta linea se convierten a tipo entero con "int"


#Calcular Promedio
promedio=(cal1+cal2+cal3)/3


#Mostrar el resultado incluyendo las calificaciones
print(f"{cal1},{cal2},{cal3}") # = print(cal1,cal2,cal3) 
print(f"El promedio de las calificaciones es:{promedio}")
# el promedio se pondra por defecto en floa ya que este esta saliendo de una division
#si quisiera controlar cuantos decimales hay que poner la sintaxi seria la siguiente: {promedio:.2f}