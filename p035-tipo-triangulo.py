# p035-tipo-triangulo
# Clasificar un triangulo segun la longitud de sus lados 

print("\033[2J\033[H")
print("Clasificador de triangulos ")

lado_a = float(input("Lado a :  "))
lado_b = float(input("Lado b :  "))
lado_c = float(input("Lado c :  "))

if lado_a == lado_b == lado_c:
    print(f"Es un triangulo EQUILATERO dado que todos sus lados son iguales")
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
    print("Es un triangulo ISOCELES, dado que dos lados son iguales")
else:
    print("Es un triangulo ESCALENO, los tres lados son diferentes")


print("\nProceso temrinado...")