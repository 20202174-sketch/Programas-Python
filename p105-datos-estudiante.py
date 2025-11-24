# p105-datos-estudiante.py
# Gestion de datos de estudiantes usando diccionarios

print('\033[H\033[J')
print('Gestión de datos de estudiantes')

estudiante = {
    'nombre':'Juan Perez',
    'edad':45,
    'email':'jperez@msn.com',
    'carrera':'Sistemas'
}

print(f'\nEl diccionario original: \n\n{estudiante} - len{estudiante}')

estudiante['calificacion'] = 9.5
estudiante['email'] = 'juanp@gmail.com'
print(f'\nEl diccionario actualizado: \n\n{estudiante} - - len{estudiante}')
print('\nLas llaves del diccionario: \n')

print('\nIterar por las llaves')
for k in estudiante.keys():
    print(k)

print('\nIterar por los valores')
print('\nLos valores del diccionario: \n')
for v in estudiante.values():
    print(v)

print("\nIterar por los elementos (items):\n")
for k, v in estudiante.items():
    print(f'{k:<10} : {v}')