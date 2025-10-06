# p038-dia-semana
# solicite un número entero del 1 al 7 y muestre el día de la semana
# correspondiente, considerando que 1 es domingo y 7 es sábado. Si el número ingresado está fuera de ese rango, debe mostrar un mensaje de error.


print("\033[2J\033[H")
day = int(input("Entrada: "))

if day >= 1 and day <= 7:
    if day == 1:
        print("Salida: Domingo")
    elif day == 2:
        print("Salida: Lunes")
    elif day == 3:
        print("Salida: Martes")
    elif day == 4:
        print("Salida: Miercoles")
    elif day == 5:
        print("Salida: Jueves")
    elif day == 6:
        print("Salida: Viernes")
    elif day == 7:
        print("Salida: Sabado")
else:
     print(f"\033[31m\nSalida: Error: dia invalido \033[0m")

