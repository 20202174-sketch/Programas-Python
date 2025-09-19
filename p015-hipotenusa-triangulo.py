#p015-hipotenusa-triangulo
#calcula la longitud de la hipotenusa de un triángulo rectángulo.

import math

#Solicitar longitud de los catetos al usuario
cateto1=float(input("Ingresa el valor del primer cateto: "))
cateto2=float(input("Ingrese el valor del segundo cateto: "))


#formula para obtener la hipotenusa
hipotenusa=math.sqrt(cateto1**2 + cateto2**2) #Elevado por potencia

hipotenusa1=math.sqrt(cateto1*cateto1 + cateto2*cateto2) #Multiplicado por si mismo

print(f"La hipotenusa de tu triangulo rectangulo es: {hipotenusa} \nLa hipotenusa con un segundo metodo es: {hipotenusa1} ")