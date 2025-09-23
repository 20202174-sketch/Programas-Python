# p034-tipo-angulo
# Mostrar el tipo de angulo
# <90 agudo, =90 Recto, <180 Obtuso, =180 llano, <360 Concavo, =360 Completo

print("\033[2j\033[h")
print("-- Clasificador de Angulos de acuerdo a su magnitud--")

angulo = int(input("Dame un angulo en grados ? "))
if angulo < 0 or angulo > 360:
    print(f"Tu angulo {angulo} no esta en el rango de 0 a 360, por lo tanto es INVALIDO ")
else:
    if angulo < 90:
        print(f"El angulo de {angulo} grados es un angulo AGUDO")
    elif angulo == 90:
        print(f"El angulo de {angulo} grados es un RECTO")
    elif angulo < 180:
        print(f"El angulo de {angulo} grados es un angulo OBTUSO")
    elif angulo == 180:
        print(f"El angulo de {angulo} grados es un angulo LLANO")
    elif angulo < 360:
        print(f"El angulo de {angulo} grados es un angulo CONCAVO")
    else: 
        print(f"El angulo de {angulo} grados es un angulo COMPLETO O CERRADO")



print("\nProceso terminado")