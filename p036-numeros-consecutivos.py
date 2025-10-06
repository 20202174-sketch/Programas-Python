# p036-numeros-consecutivos
# Escribe un programa que reciba tres números enteros y determine si son consecutivos. Si lo son, muestra un mensaje de confirmación; de lo contrario, informa que no lo son.

print("\033[2J\033[H")
n1 = int(input("Ingresa el primer numero: "))
n2 = int(input("Ingresa el Segundo numero: "))
n3 = int(input("Ingresa el tercer numero: "))

# Primero trato de diferenciar los numeros que esten en orden
# Checo que la resta sea 1 ya que para que sean numero consecutivos siempre van a cumplir esto
if n1 < n2 and n2 < n3: 
    if n3 - n2 == 1 and n2 - n1 ==1: # el if qu eesta aqui esta anidado esto significa que si se cumple lo de arriba pasa abajo y checa si se cumple lo d esta linea "si fuer elif este checaria si se cumple lo de arriba y sino se cumple se pasa a lo de abajo (a esta linea)"
        print(f"\033[32m\nLos numeros son consecutivos!\033[0m") # le agrego color el numero 32m es verde y el numero 31m es rojo
    else:
        print(f"\033[31m\nLos numeros no son consecutivos!\033[0m")
elif n1 > n2 and n2 > n3:
    if n1 - n2 == 1 and n2 - n3 == 1:
        print(f"\033[32m\nLos numeros son consecutivos!\033[0m")
    else:
        print(f"\033[31m\nLos numeros no son consecutivos!\033[0m")
else:
    print(f"\033[31m\nLos numeros no son consecutivos!\033[0m")

    


