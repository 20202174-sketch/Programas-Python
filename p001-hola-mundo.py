#p001.hola-mundo
#Lee datos y envia un saludo

print("Leyendo datos y enviando un saludo: \n")
nombre = input("Dame tu nombre")
edad = int(input("Edad: "))
peso = float(input("peso tu Peso: "))

print("{nombre} bienvenido a python, tu edad es: {edad},tu peso es: {peso}")
#la f le da valores a las variables es para formatear la salida, con la f la salida es gabriel bienvenido a python,
#tu edad es: 23,tu peso es: 79.0 y sin la f la slaida es{nombre} bienvenido a python, tu edad es: {edad},tu peso es: {peso} 
print(type(nombre))
print( type(peso))
print( type(edad))