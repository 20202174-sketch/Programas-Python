# p037-numero-mayor
# reciba tres números enteros e identifique y muestre cuál de ellos es el mayor.

print("\033[2J\033[H")
n1 = int(input("Ingresa el primer numero: "))
n2 = int(input("Ingresa el segundo numero: "))
n3 = int(input("Ingresa el tercer numero: "))

# comparo cada uno de los numero entre ellos 
if n1 > n3 and n1 > n2:
    print(f"El numero mayr es: {n1}")
elif n2 > n1 and n2 > n3:
    print(f"El numero mayor es: {n2}")
elif n3 > n1 and n3 > n2:
    print(f"El numero mayor es: {n3}")
