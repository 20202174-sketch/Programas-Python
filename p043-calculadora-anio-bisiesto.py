# p043-calculadora-anio-bisiesto
# programa que determine si un año, ingresado por el usuario, es bisiesto.

print("\033[2J\033[H")

year = int(input("Año: "))

if year % 4 == 0 and not (year % 100 == 0):
    print(f"El año {year} es bisiesto. (Porque es divisible por 4 pero no por 100).")
elif year % 100 == 0 and not(year % 400 == 0):
    print(f"El año {year} no es bisisesto. (Porque es divisible por 100 pero no por 400).")
elif year % 400 == 0:
    print(f"El año {year} es bisiesto. (Porque es divisible por 400).")
elif not (year % 4 == 0):
    print(f"El año {year} no es bisiesto. (Porque no es divisible por 4).")





