#p019-calculo-tiempo
#programa que toma una cantidad de horas como un número entero.


#Solicito al usuario el numero de horas
horas = int(input("Dame la cantidad de horas: "))


#Formulas para calular los dias, minutos y segundos.
dias = horas // 24 # para calcular los dias solo se hace una division, tiene doble simbolo // para que me arroje un resultado entero, porque python si le dejas un solo / simbolo si hace la division pero en automatico la convierte a float 
minutos = horas * 60 
segundos = horas * 60 * 60


#Se imprimen los resultados para mostrarlos a usuario
print(f"Tus horas son equivalentes a: {dias} Dias, {minutos} Minutos, y {segundos} Segundos.")