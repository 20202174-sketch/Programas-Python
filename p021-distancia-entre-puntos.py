#p021-distancia-entre-puntos
#calcula la distancia entre dos puntos en un plano cartesiano.

import math

#Soliciar al usuario pedir las coordenadas (x,y) del punto A y las coordenadas (x,y) del punto B
print("Ingresa la coordenada x,y del punto A separada por un espacio y da enter: ")
ax,ay = input().split()
ax,ay = int(ax),int(ay)

print("Ingresa la coordenada x,y del punto B separada por un espacio y da enter: ")
bx,by = input().split()
bx,by = int(bx),int(by)


#Calcular la distancia
distancia = math.sqrt(((ax-bx)**2) + ((ay - by)**2))
print(f"La distancia entre tus dos puntos es: {distancia}")