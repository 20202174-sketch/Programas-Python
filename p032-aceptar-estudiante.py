# p032-aceptar-estudiante
# Aceptar a un estudiante en base a la edad y 2 calificaciones 
# usaremos or 

print("\033[2J\033[H")
print("---Admision de estudiantes a la universidad sierra madre ---")

nombre = input("Dame tu nombre ? ")
edad = int(input("Edad ? "))

if edad < 18 :
    print(f"Lo sentimos {nombre}, Solo aceptamos mayores de edad, y tu tienes tan solo {edad} !")
else:
    print("Ingresa 2 Calificaciones separadas por Enter")
    calificacion1 = float(input())
    calificacion2 = float(input())
    if calificacion1 < 8 or calificacion2 < 8:
        print(f"Lo sentimos, se requieren 2 calificaciones de 8 como minimo, y tu tienes {calificacion1}, {calificacion2}")
    else:
        print(f"!Bienvenido {nombre}, tu edad de {edad} y tus calificaciones: {calificacion1},{calificacion2} te permiten ingresar")
        
print("\nProceso Terminado")