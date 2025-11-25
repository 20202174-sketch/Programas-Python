# p155-estadisticas-basicas.py
# Crea un programa que calcule estadísticas básicas (poblacionales) para una lista de números. El programa debe
# incluir:
# 1. Una función para leer una lista de números enteros.
# 2. Funciones separadas para calcular y devolver cada una de las siguientes estadísticas:
# o Número mayor
# o Número menor
# o Media (promedio)
# o Varianza poblacional
# o Desviación estándar poblacional

# El programa principal debe leer la lista e imprimir todos los resultados estadísticos de forma clara.

def leer_numeros() -> list[int]:
    cadena = input("Ingresa los números separados por espacio: ")
    partes = cadena.split()
    lista = []
    for item in partes:
        lista.append(int(item))
    return lista


def obtener_mayor(valores: list[int]) -> int:
    maximo = valores[0]
    for v in valores:
        if v > maximo:
            maximo = v
    return maximo


def obtener_menor(valores: list[int]) -> int:
    minimo = valores[0]
    for v in valores:
        if v < minimo:
            minimo = v
    return minimo


def calcular_media(valores: list[int]) -> float:
    acumulado = 0
    for v in valores:
        acumulado += v
    return acumulado / len(valores)


def calcular_varianza(valores: list[int]) -> float:
    prom = calcular_media(valores)
    suma = 0
    for v in valores:
        suma += (v - prom) ** 2
    return suma / len(valores)     # varianza poblacional


def calcular_desviacion(valores: list[int]) -> float:
    return calcular_varianza(valores) ** 0.5


def ejecutar() -> None:
    nums = leer_numeros()

    print(f"Lista proporcionada: {nums}")
    print("Estadísticas calculadas:")
    print(f"Media: {calcular_media(nums)}")
    print(f"Mayor: {obtener_mayor(nums)}")
    print(f"Menor: {obtener_menor(nums)}")
    print(f"Varianza: {calcular_varianza(nums)}")
    print(f"Desviación estándar: {calcular_desviacion(nums)}")


if __name__ == "__main__":
    ejecutar()
