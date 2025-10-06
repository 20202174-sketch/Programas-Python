# p042-precio-entrada-cine.py
# programa para la taquilla de un cine que determine el precio de una entrada según la edad del
# cliente. El programa debe solicitar la edad y mostrar el precio correspondiente.

print("\033[2J\033[H")

age = int(input("Edad: "))

if age < 5:
    print("Tu entrada es gratis")
elif age >= 5 and age <= 12:
    print("El precio de tu entrada es de $5")
elif age >=13 and age <=64:
    print("El precio de tu entrada es de $10")
elif age >= 65:
    print("El precio de tu entrada es $7")
