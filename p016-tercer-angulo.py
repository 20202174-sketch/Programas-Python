#p016-tercer-angulo
#determina el tercer ángulo de un triángulo.

print("="*60)
print("  Este programa determina el tercer angulo de un triángulo")
print("="*60)


#Solicitar angulos al usuario
angulo1=float(input("Ingresa la medida de un primer angulo en grados: "))
angulo2=float(input("Ingresa la medida de un segundo angulo en grados:  "))

#Formula para obtener el tercer angulo
angulo3=180-(angulo1 + angulo2)

#Imprime en pantalla el resultado
print(f"El angulo que te falta es de: {angulo3}°")