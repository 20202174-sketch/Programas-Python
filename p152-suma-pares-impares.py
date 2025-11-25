# p152-suma-pares-impares.py
# Crea un programa que sume números pares o impares dentro de un rango especificado. El programa debe tener
# una función que reciba tres parámetros: un número de inicio, un número de fin y una letra ('P' o 'I').
# • Si la letra es 'P', la función debe devolver la suma de todos los números pares en ese rango (incluyendo
# los límites).
# • Si la letra es 'I', la función debe devolver la suma de todos los números impares en el rango.
# El programa principal debe mostrar un menú, pedir los datos al usuario y mostrar el resultado de la suma.


def sumar_en_rango(inicio: int, fin: int, opcion: str) -> tuple[int, list[int]]:
    total = 0
    terminos = []

    for numero in range(inicio, fin + 1):
        if opcion == "P" and numero % 2 == 0:
            total += numero
            terminos.append(numero)
        elif opcion == "I" and numero % 2 != 0:
            total += numero
            terminos.append(numero)

    return total, terminos


def ejecutar() -> None:
    print("*** Suma en Rango ***")

    ini = int(input("Ingresa el límite inicial: "))
    fin = int(input("Ingresa el límite final: "))
    letra = input("¿Qué deseas sumar? (P)ares o (I)mpares: ").strip().upper()

    if letra not in ("P", "I"):
        print("Error: opción incorrecta.")
        return

    suma, terminos = sumar_en_rango(ini, fin, letra)

    if letra == "P":
        print(f"La suma de los números pares entre {ini} y {fin} es: {suma}")
    else:
        print(f"La suma de los números impares entre {ini} y {fin} es: {suma}")

    if terminos:
        expresion = " + ".join(str(n) for n in terminos)
        print(f"(Cálculo: {expresion} = {suma})")
    else:
        print("No hay números que cumplan la condición en ese rango.")


if __name__ == "__main__":
    ejecutar()
