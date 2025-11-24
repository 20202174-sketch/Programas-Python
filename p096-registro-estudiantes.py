# p096-registro-estudiantes.py
# Registro y análisis de asistentes a un evento
print('\033[H\033[J')

print('Sistema de Registro para Evento\n')
print("Introduce los nombres y edades de los asistentes (* en nombre para terminar)\n")

nombres = []
edades = []

while True:
    nombre = input("Nombre del asistente: ")
    if nombre == "*":break 
    try:
        edad = int(input(f"Edad de {nombre}: "))
        nombres.append(nombre) 
        edades.append(edad) 
    except ValueError:
        print("Por favor, introduce una edad válida (número entero).")

if not nombres:
    print("\nNo se registraron asistentes.")
else:

    print("\n--- Asistentes Mayores de Edad ---")
    encontrados = False
    for i in range(len(nombres)):
        if edades[i] >= 18:
            print(f"Nombre: {nombres[i]}, Edad: {edades[i]}")
            encontrados = True

if not encontrados:
    print("No hay asistentes mayores de edad.")


edad_maxima = max(edades)
posicion_max = edades.index(edad_maxima) 
nombre_max = nombres[posicion_max]
print("\n--- Reconocimiento al Asistente de Mayor Edad ---")
print(f"El asistente de mayor edad es: {nombre_max} con {edad_maxima} años.")