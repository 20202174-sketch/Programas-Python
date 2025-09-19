#p020-numero-suerte
#Solicita al usuario su año de nacimiento como un número entero de cuatro dígitos.


# Solicitar al usuario su año de nacimiento
anio = input("Ingresa tu año de nacimiento (4 dígitos): ")

# Mostrar cada uno de los dígitos
print("Dígitos individuales del año:")
for digito in anio:
    print(digito)

# Calcular la suma de los dígitos
suma = sum(int(d) for d in anio)

print("La suma de los dígitos es:", suma)
