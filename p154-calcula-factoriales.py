# p154-calcula-factoriales.py
# Desarrolla un programa que calcule el factorial de cada número en una lista. Debes implementar:
# 1. Una función que lea y devuelva una lista de números enteros.
# 2. Una función que reciba un número entero y devuelva su factorial (ej: 5 -> 120).
# 3. Una función principal que reciba la lista de números. Esta debe usar la función factorial para crear y
# devolver una nueva lista con los factoriales de cada número.
# El programa debe imprimir la lista original y la lista de factoriales.

def leer_numeros() -> list[int]:
    datos = input("Ingresa los números separados por espacio: ")
    partes = datos.split()
    lista = []

    for elemento in partes:
        lista.append(int(elemento))

    return lista


def obtener_factorial(n: int) -> int:
    total = 1
    for k in range(1, n + 1):
        total *= k
    return total


def generar_factoriales(valores: list[int]) -> list[int]:
    resultado = []
    for numero in valores:
        resultado.append(obtener_factorial(numero))
    return resultado


def ejecutar() -> None:
    nums = leer_numeros()
    lista_fact = generar_factoriales(nums)

    print(f"Lista original: {nums}")
    print(f"Lista con factoriales: {lista_fact}")


if __name__ == "__main__":
    ejecutar()
