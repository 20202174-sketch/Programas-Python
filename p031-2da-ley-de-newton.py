# p031-2da-ley-de-newton
# Calcular la segunda ley de newton
# fuerza = masa * aceleracion, masa = fuerza / aceleracion, aceleracion = fuerza / masa

print("\033[2J\033[H")
print("Calcular los valores de la segunda ley de newton")
print("[ F ] uerza        = masa * aceleracion")
print("[ M ] asa          = fuerza / aceleracion")
print("[ A ] celeracion   = fuerza / masa")
opcion = input ("Elige una opcion ? ").upper()

if opcion == "F":
    print("\nCalculadno la fuerza")
    masa = float(input("Masa ?"))
    aceleracion = float(input("Aceleracion ? "))
    fuerza = masa * aceleracion
    print(f"\nLa fuerza es: {fuerza}")
elif opcion == "M":
    print("\nCalculando la masa")
    fuerza = float(input("Fuerza ? "))
    aceleracion = float(input("Aceleracion ? "))
    masa = fuerza / aceleracion
    print(f"\nLa masa es: {masa}")
elif opcion == "A":
    print("\nCalculando la Aceleracion")
    fuerza = float(input("Fuerza ? "))
    masa = float(input("Masa"))
    aceleracion = fuerza / masa
    print(f"\nLa Aceleracion es :{aceleracion}")
