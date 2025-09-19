#p017-convertir-temperatura
#convierte una temperatura de grados Celsius a grados Fahrenheit y el color de las letras cambia en tres colores dependiendo la temperatura.

print("="*65)
print("  Este programa convierte de grados Celsius a grados Farenheit")
print("="*65)


#Pedir la temperatura al usuario
celsius=float(input("Ingresa la Temperatura en grados Celsius que quieras convertir: "))

#Calcular grados Farenheit
farenheit = (celsius * 9/5) + 32

#Mostrar datos convertidos al usuario dependiendo de las temperatura el color de las letras cambiara para dar idea de si es una alta o baja temperatura
if celsius <=10:
    print(f"\033[94m\nTus {celsius}° grados Celsius Equivalen a {farenheit}° grados Farenheit\033[0m")
if celsius >10 and celsius<20:
    print(f"\033[97m\nTus {celsius}° grados Celsius Equivalen a {farenheit}° grados Farenheit\033[0m")
if celsius >=20:
    print(f"\033[91m\nTus {celsius}° grados Celsius Equivalen a {farenheit}° grados Farenheit\033[0m")

