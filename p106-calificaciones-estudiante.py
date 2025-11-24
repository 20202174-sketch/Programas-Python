# p106-calificaciones-estudiante.py
# Gestion de calificaciones de un estudiante usando diccionarios

print('\033[H\033[J')
print('Gestion de calificaciones de un estudiante usando diccionarios')

materias = ['Fisica', 'Quimica', 'Matematicas', 'Geografia', 'Estadistica']
califs = [10, 9, 8, 7.5, 6]

print(f'Lista de materias : \n{materias}')
print(f'Lista de calficaciones: \n{califs}')

notas = dict(zip(materias, califs))

print(f'Las notas', notas)

notas.update({'Ingles':10, 'Programacion':7})

print(f'\nSe agregaron elementos) : \n{notas} - {len(notas)}')

notas.pop('Fisica')
notas.popitem()
print(f'\nSe removieron elementos : \n{notas} - {len(notas)}')

notas.update({'Quimica':10, 'Matematicas':10})

print(f'\nSe modificaron elementos : \n{notas} - {len(notas)}')

s = 0
print('\nMaterias y calificaciones finales')
for m, c in notas.items():
    print(f'{m:<12} - {c:5}')
    s += c

print(f'\nLa suma: {s}')
print (f'El promedio es: {s/len(notas)}')

notas.clear()
print(f'\nLas notas: {notas} - {len(notas)}')