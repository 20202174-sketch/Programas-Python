# p072-pares-impares.py
# Imprimir numeros pares e impares y su suma, el usuario elige

while(True):
    print('\033[H\033[J')
    print('Imprimir numeros pares e impares y su suma')
    print('[ 1 ] Pares ')
    print('[ 2 ] Impares ')
    op = int(input('Elige ? '))
    
    s = 0
    if op==1:
        print(f'\nImprimir numeros pares y su suma')#{n}
        n = int(input('Limite ? '))
        for i in range(2,n+1, 2):
            print(i, end=' ')
            s += i
        print('\suma  de pares:'+ str(s))
    elif op==2:
        print(f'\nImprimir numeros impares y su suma')
        n = int(input('Limite? '))
        for i in range(n, +1, 2):
            print(i, end=' ')
            s += i
        print('\suma  de impares:'+ str(s))

    else:
        print('\nOpción No valida')
    
    if input('\n\nDeseas continuar ( S / N ) ? ').upper()=='N': break

print('\nProceso terminado')