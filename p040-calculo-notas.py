# p040-calculo-notas
# calcule el promedio de 5 calificaciones ingresadas por el usuario. Basado en el
# promedio, el programa deberá mostrar uno de los siguientes mensajes:
# • Menor a 6: "Quedas reprobado"
# • Desde 6 hasta menos de 7: "Pasas de panzazo"
# • Desde 7 hasta menos de 8: "Muy bien, puedes mejorar"
# • Desde 8 hasta menos de 9: "Excelente, sigue así"
# • Desde 9 hasta 10: "Perfecto, tu esfuerzo valió la pena"

print("\033[2J\033[H")


entrada = input("Ingresa 5 numeros separados por coma: ")

# Separar por comas y convierte cada uno en entero 
n1, n2, n3, n4, n5 = map(int, entrada.split(","))

prom = (n1 + n2 + n3 + n4 + n5) / 5

if prom <= 6:
    print(f"Tu promedio es: {prom} quedas reprobado")
elif prom == 7:
    print(f"Tu promedio es: {prom} Pasas de panzazo")
elif prom == 8:
    print(f"Tu promedio es: {prom} Muy bien, puedes mejorar")
elif prom == 9:
    print(f"Tu promedio es: {prom} Excelente, sigue asi")
elif prom == 10:
    print(f"Tu promedio es: {prom} Perfecto, tu esfuerzo valio la pena")
else:
    print("Ocurrio un error como nota tus calificaciones solo pueden ser del 1-10")

