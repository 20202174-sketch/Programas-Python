# p045-conteo-ascendente-v2.py
# Imprime los números de 1 a n, en incrementos de m, usando un ciclo while

print("\033[2J\033[H")
print("Iniciando secuencia de conteo ascedente")

n = int(input("Hasta que numero? "))

m = int(input("De cuanto en cuanto es el incremento? "))

b = m 
while b <= n:
    print(f" {b}",end="")
    b += m


print("\n Secuencia completada")