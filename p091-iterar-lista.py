# p091-iterar-lista.py
# Iterar por los elementos de una lista
print('\033[H\033[J')

print('Iterar por los elementos de una lista:\n')

nums = [2, 4, 6, 8, 10, 12, 14, 16]

print(f'Números a procesar: {nums} - {len(nums)}\n')

print('1. Iteración por elemento:')
for n in nums:
    print(n, end=' ')

print('\n\n2. Iteración por indice de cada elemento:')
for i in range(len(nums)):
    print(nums[i], end=' ')

print('\n\n3. Iteración por elemento para sumar 2')
for n in nums:  
    print(n + 2, end=' ')

print('\n\n4. Iteración por índice para sumar 10')
for i in range(len(nums)):
    print(nums[i]+10, end=' ')

print('\n\n5. Iteración con enumerate')
for i, n in enumerate(nums):
    print(i,'\t', n,)

print(f'\n\nResultado: {nums} - {len(nums)}')

print(f'Modificar la lista al iterar')
for n in nums:
    n = n ** 2

print(f'\n\nResultado: {nums} - {len(nums)}')