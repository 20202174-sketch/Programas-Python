# p129-func-param-nombre.py

def saluda(apaterno: str, amaterno: str, nombre: str, edad: str) -> None:
    print(f'Hola {nombre} {apaterno} {amaterno}, tienes {edad} años de edad...')

saluda('Lopez', 'Martinez', 'Ana', '25')
saluda(nombre='Ana', amaterno='Martinez', apaterno='Lopez')
saluda(nombre='Juan',apaterno='Diaz', edad='19', amaterno='Lopez')