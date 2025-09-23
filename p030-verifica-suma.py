# p030-verifica-suma.py
# Verifica si la suma de dos números es igual a un tercero
# 10 2 12  5 7 2  10 8 2  6 6 6  1 9 5 

print("\033[2J\033[H")
print("---Verificar si la suma de dos numeros es igual a un tercero")


#entrada 
print("Dame 3 numeros enteros separados por un espacio :")
n1, n2, n3 = input().split()
n1, n2, n3 = int(n1), int(n2), int(n3)

#proceso
if n1+n2 == n3 : 
    print(f"{n1} + {n2} = {n3}")
elif n1 + n3 == n2:
    print(f"{n1} + {n3} = {n2}")
elif n2 + n3 == n1:
    print(f"{n2} + {n3} = {n1}")
elif n1 == n2 == n3 : 
    print(f"{n1} , {n2} , {n3} son iguales !")
elif n1 != n2 != n3:
    print(f"{n1} , {n2} , {n3} Todos son diferentes !")
else:
    print(f"Es probable que {n1} , {n2} , {n3} sea un par igual")

print("Proceso terminado")