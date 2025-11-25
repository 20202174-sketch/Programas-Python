# p153-suma-digitos.py
# Escribe un programa que procese una lista de números. Debes implementar lo siguiente:
# 1. Una función que lea y devuelva una lista de números enteros (puedes reusar la hecha en clase).
# 2. Una función que reciba un número entero y devuelva la suma de sus dígitos individuales (ej: 1971 ->
# 1+9+7+1 = 18).
# 3. Una función principal que reciba la lista de números. Esta debe usar la función anterior para crear y
# devolver una nueva lista que contenga la suma de los dígitos de cada número original.
# El programa debe imprimir la lista original y la nueva lista con las sumas.

def leer_numeros() -> list[int]:
    datos = input("Ingresa los números separados por espacio: ")
    partes = datos.split()
    lista = []

    for elem in partes:
        lista.append(int(elem))

    return lista


def sumar_digitos(num: int) -> int:
    total = 0
    for caracter in str(num):
        total += int(caracter)
    return total


def generar_lista_sumas(lista: list[int]) -> list[int]:
    nueva = []
    for valor in lista:
        nueva.append(sumar_digitos(valor))
    return nueva


def ejecutar() -> None:
    nums = leer_numeros()
    lista_convertida = generar_lista_sumas(nums)

    print(f"Lista original: {nums}")
    print(f"Lista con sumas de dígitos: {lista_convertida}")


if __name__ == "__main__":
    ejecutar()
