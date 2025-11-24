#p053-conjetura-collatz.py
# Calcuar la conjetura de collatz

while True:
    print('\033[H\033[J')

    print('Imprime la conjetura de collatz')
    pasos=0
    while True:
        num = int(input('Dame un número = '))
        if num > 0: break
        print('Error, el número debe ser mayor que 0')
        print('\nLa conjetura de collatz es:')

    while True:
        if num == 1: break
        print(num,end=' ')
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
        pasos = pasos + 1

    print(num,end=' ')

    print('\nPasos :'  + str(pasos+1))
    if input('\n\nDeseas Continuar(S/N)? ').upper()=='N': break
