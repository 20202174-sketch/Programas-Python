# p070-conteo-descendente-for-v2.py
# Imprime los numeros de n a 1, en decrementos de m. usando un ciclo for

print ('\033[H\033[J')
print('Iniciando secuencia ascendente')

n = int(input('Hasta donde?'))
m = int(input('De cuanto en cuanto'))

for f in range (n, 0, -m ):
    print(f, end=' ')