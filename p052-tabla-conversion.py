#p052-tabla-conversion.py
# Mostrar una tabla de conversion de Peso a Dolares 

tc = 20.71

while True:
    print('\033[h\033[J')

    print('Tabla de conversion de peso a dolar')
    print(f'Tipo de cambio : {tc} pesos x dolar')
    print('-'*15)

    while True: # Valida los valores inicial y final
        pi = float(input('valor inicial : '))
        pf = float(input('valor final : '))
        if (pi>0 and pf>0) and (pi<pf): break
        print("Error en los valores, intente de nuevo")
    
    c = pi
    print("\nPesos\tDollar")
    print("-"*15)
    while c <= pf : #Construye la tabla
        print(f'{c}\t{c/tc:.2f}')
        c+=1
    print("-"*25)
    
    if input('Deseas continuar (S/N)? ').upper()=='N': break