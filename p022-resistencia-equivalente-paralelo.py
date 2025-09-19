#p022-resistencia-equivalente-paralelo
#calcule la resistencia total o equivalente de un circuito con cuatro resistencias en paralelo.

print("="*50)
print("Calculadora de resisencia total con 4 resistencias")
print("="*50)


print("\nIngresa el valor de tus 4 resisencias separada por un espacio y da enter: ")
r1,r2,r3,r4 = input().split()
r1,r2,r3,r4 = float(r1),float(r2),float(r3),float(r4)

#Se hace el calculo con respecto a la ecuacion
rt = 1 / ((1/r1) + (1/r2) + (1/r3) + (1/r4))

print(f"Tu resistencia total es de: {rt}")