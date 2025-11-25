# p132-funcion-retorno.py

def suma(n1:float, n2:float, n3:float) -> float:

    return n1 + n2 + n3

print('\nSuma de dos numeros constantes: ')

suma_resultado = suma(10,20,30)
print(f"La suma es {suma_resultado:,.2f}")

print('\nDame tres numeros separados por enter: ')
a,b,c = float(input()), float(input()), float(input())

print(f"La suma de los numeros es {suma(a,b,c):,.2f}")