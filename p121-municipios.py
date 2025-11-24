# p121-municipios.py
# Gestion de un padrón municipal

municipios = {'Zacatecas', 'Guadalupe', 'Jerez', 'Fresnillo', 'Fresnillo'}

print('\033[H\033[J')
print(' Gestión de Municipios (con Conjuntos)\n')

print(f'Los municipios: {municipios} - {len(municipios)} - {type(municipios)}')

print("\nLista de municipios registrados:")
for mun in municipios:
    print(mun, end=' | ')

print('\nAltas en el Padrón')
municipios.add('Teul')
print(f'Municipios: {municipios} - {len(municipios)}')

print('\nAgregar varios municipios al padron ---')
municipios.update({"Luis Moya", "Ojocaliente", "Tepetongo"})
print(f'Municipios: {municipios} - {len(municipios)}')

print("\nBajas del Padrón")
municipios.remove('Zacatecas')
print(f'Municipios remove(): {municipios} - {len(municipios)}')

municipios.discard("Ojocaliente")
print(f'Municipios discard(): {municipios} - {len(municipios)}')
mun_eliminado = municipios.pop()

print(f'Baja con Pop() (elemento arbitrario): \n{municipios} \nEliminado:{mun_eliminado}\n')
municipios.clear()
print(f'Municipios pop(): {municipios} - {len(municipios)}')