# p123-conjunto-personas.py
# Manejo básico de conjuntos con nombres

print('\033[H\033[J')
print('--- Administrador de Conjuntos ---\n')

lista1 = ['Juan', 'Maria', 'Pedro', 'Jose', 'Rocio']
lista2 = ['Pedro', 'Juan', 'Pablo', 'Mateo', 'Esther']

# Crear conjuntos
A = set(lista1)
B = set(lista2)

print('Conjuntos creados:')
print(f'A (desde lista1): {A}')
print(f'B (desde lista2): {B}')

# Operaciones
print('\nOperaciones entre A y B')
print(f'Unión: {A | B}')
print(f'Intersección: {A & B}')
print(f'Diferencia A-B: {A - B}')
print(f'Diferencia Simétrica: {A ^ B}')

# Comprobaciones
conj_sub = {'Pablo', 'Mateo'}
conj_super = {'Reynaldo', 'Angelica'}

print('\nVerificaciones:')
print(f'¿{{Pablo, Mateo}} ⊆ B? : {conj_sub <= B}')
print(f'¿A es superconjunto de {{Reynaldo, Angelica}}? : {A >= conj_super}')
print(f'¿"Pedro" pertenece a A? : {"Pedro" in A}')
print(f'¿"Lilia" NO está en B? : {"Lilia" not in B}')
