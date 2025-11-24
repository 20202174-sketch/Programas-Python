# p124-conjunt-numeros.py
# Manejo de conjuntos a partir de listas numéricas

print('\033[H\033[J')
print('--- Análisis de Conjuntos Numéricos ---\n')

lista1 = [50, 60, 70, 80, 90, 100, 200]
lista2 = [60, 90, 100, 300, 400, 500]
lista3 = [10, 20, 60, 90, 70, 100, 600, 700]

# Crear conjuntos desde las listas
A = set(lista1)
B = set(lista2)
C = set(lista3)

print('Conjuntos generados:')
print(f'A = {A}')
print(f'B = {B}')
print(f'C = {C}')

# Operaciones solicitadas
print('\nResultados de las operaciones:')
print(f'A ∪ B : {A | B}')
print(f'B ∪ C : {B | C}')
print(f'A - C : {A - C}')
print(f'B ^ C : {B ^ C}')
print(f'B ∩ C : {B & C}')

# Verificaciones lógicas
print('\nComprobaciones:')
print(f'¿A es subconjunto de B? : {A <= B}')
print(f'¿C es subconjunto de A? : {C <= A}')
print(f'¿100 pertenece a A? : {100 in A}')
print(f'¿60 está en A, B y C? : {(60 in A) and (60 in B) and (60 in C)}')
print(f'¿900 no está en C? : {900 not in C}')
