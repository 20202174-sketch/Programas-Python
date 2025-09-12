#p005-calculadora-ims
#calcula el indice de masa corporal

print("Calculando el indice de masa corporal (IMC)\n")

peso_kg = float( input("Ingresa tu peso en kilogramos: "))
altura_m = float( input("Ingresa tu altura en metros: "))

#Proceso
imc = peso_kg / (altura_m ** 2)# divide el peso entre la altura al cuadrado (** elevada a la potencia)

#Salida
print("El peso es {0:.2f}kg y la altura es {1:.2f}m".format(peso_kg,altura_m))
 
print(f"El peso es {peso_kg:.2f}kg y la alura es {altura_m:.2f}y resulta en un IMC de {imc:.2f}")
