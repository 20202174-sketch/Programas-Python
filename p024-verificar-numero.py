#p024-verificar-numero
#Verifica si un numero es positivo, negativo, o cero

print("Verificando si un numero es positivo")

#entrada
print("Dame un numero entero ?")
numero = int(input())

#Proceso
if numero ==0:
    print("El numero es CERO")
else:
    if numero<0:
        print("el numero es negativo")
    else:
        print("El numero es positivo")
print("\nProceso terminado")
