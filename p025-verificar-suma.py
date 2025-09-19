#p025-verificar-suma
#Verificar si la suma de dos numeros es igual a un tercero

print("-"*60)
print("Verificar si la suma de dos numeros es igual a un")
print("-"*60)

print("\nDame 3 numeros enteros : ")
n1 = int(input("Numero 1 ? "))
n2 = int(input("Numero 2 ? "))
n3 = int(input("Numero 3 ? "))

#proceso
suma = n1 + n2

if suma == n3:
    print(f"\n !Correcto! {n1} + {n2} ES IGUAL {n3}")
else:
    print(f"\n No coinciden {n1} + {n2} NO ES IGUAL {n3}")

print("-"*60)
print("\nFin del programa")