# p149-numero-menor.py
# Crea un programa que incluya una función. Dicha función debe solicitar 3 números enteros al usuario y devolver el menor.

def obtener_menor() -> int:
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    c = int(input("Ingresa el tercer número: "))

    minimo = a
    if b < minimo:
        minimo = b
    if c < minimo:
        minimo = c

    return minimo


def iniciar() -> None:
    menor = obtener_menor()
    print(f"El número menor es: {menor}")


if __name__ == "__main__":
    iniciar()
