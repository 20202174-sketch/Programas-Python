# p073-suma-promedio-numeros.py
# Suma y promedio de n numeros introducidos por el usuario usando ciclo for

while(True):
    print('\033[H\033[J')
    print('Sumando y promediando numeros')

    n = int(input('Cuantos numeros deseas procesar ? '))
    s = 0
    numeros = ""

    for i in range(1, n+1):
        cal = int(input(f'Calificacion[{i}] = '))
        s += cal
        numeros = numeros + str(cal) + ' '

    print(f'Las calificaciones fueron {numeros}')
    print(f'La suma es: {s}')
    print(f'El promedio es {s / cal}')

    if input('\n\nDeseas continuar (S/N) ? ').upper()=='N': break
    
    print('\nProceso terminado ....')