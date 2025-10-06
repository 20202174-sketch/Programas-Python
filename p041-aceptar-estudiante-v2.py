# p041-aceptar-estudiante-v2
# programa que solicite el nombre, sexo (h/m), edad y tres calificaciones de un aspirante. El programa
# debe evaluar los datos y mostrar un mensaje claro que indique si el estudiante fue aceptado. Si no es aceptado, el
# mensaje debe especificar la razón del rechazo (ya sea por no cumplir con el sexo, la edad o el promedio
# requerido).

print("\033[2J\033[H")


name = input("Nombre: ")
sex = input("Sexo (H/M): ")
age = int(input("Edad: "))
cal = input("Son 3 calificaciones solo ve agregandolas todas en esta linea y separalas por una coma ;) Calificaciones: ")
c1, c2, c3 = map(float, cal.split(","))
prom = (c1 + c2 + c3) / 3


if not (sex == "M" or sex == "m"):
    print(f"Lo sentimos, {name}. La universidad acepta solo mujeres.")
elif not (age > 21):
    print(f"Lo sentimos, {name}. No cumples con la edad requerida (mayor de 21).")
elif not (prom >= 8 and prom <= 10):
    print(f"Lo sentimos, {name}. Tu promedio de {prom:.2f} no alcanza el mínimo requerido (8.00).")
else:
    print(f"Felicidades, {name}! Has sido aceptada. "
          f"Cumples con el sexo, la edad y tu promedio de {prom:.2f} está dentro del rango permitido.")

