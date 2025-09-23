# p033-aceptar-estudiante-v2
# Aceptar un estudiante en base a la edad y 2 calificaciones 
# usaremos and

print("\033[2J\033[H")
print("--- Admision de estudiantes a la Universidad Sierr Madre ---")

nombre = input("Dame tu nombre ? ")
edad = int(input("Edad ? "))

if edad >= 18:
    print("El proceso continua")
    calificacion1 = float(input())
    calificacion2 = float(input())
    if calificacion1 >= 8 and  calificacion2 >=8:
        print(f"!Bienvenido {nombre}, tu edad {edad} y tus calificaciones: {calificacion1}, {calificacion2} te permite ingresar")
    else:
        print(f"Lo sentimos, se requieren 2 calificaciones de 8 como minimo, y tu tienes {calificacion1}, {calificacion2}")
else:
    print(f"\nLo sentimos {nombre}, Solo aceptamos mayores de edad y tu tienes {edad} años")

print("\nProceso terminado ...")