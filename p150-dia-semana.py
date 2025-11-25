# p150-dia-semana.py
# Escribe un programa con una función que reciba un número entero entre 1 y 7. La función debe devolver el día
# de la semana correspondiente en texto (ej: 1 = "Lunes", 7 = "Domingo"). El programa principal debe pedir el
# número al usuario, llamar a la función y mostrar el nombre del día.

def obtener_dia(valor: int) -> str:
    semana = [
        "Lunes",
        "Martes",
        "Miércoles",
        "Jueves",
        "Viernes",
        "Sábado",
        "Domingo"
    ]

    if valor >= 1 and valor <= 7:
        return semana[valor - 1]
    else:
        return None


def ejecutar() -> None:
    num = int(input("Escribe un número entre 1 y 7: "))
    dia = obtener_dia(num)

    if dia is None:
        print("Error: Debe ser un número válido entre 1 y 7.")
    else:
        print(f"El día correspondiente es: {dia}")


if __name__ == "__main__":
    ejecutar()
