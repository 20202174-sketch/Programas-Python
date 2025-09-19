#p027-calcular-paga-extra
#Calcula la paga de un trabajador considerando las horas extra (se pagan al doble)

print("\033[2J\033[H")
print("Calculando la paga extra de un trabajador")

#entrada
print("Introduce los datos del trabajador")
nombre = input("Nombre ? ")
horas = int(input("Horas trabajadas ? "))
paga_hora = float(input("Paga por hora"))

#proceso
horas_normales = 40
paga_normal = 0
paga_extra = 0
total = 0
if horas <= horas_normales:
    paga_normal = horas * paga_hora
    total = paga_normal
else:
    paga_normal = horas_normales * paga_hora
    horas_extra = horas - horas_normales
    paga_extra = horas_extra * (paga_hora * 2)
    total = paga_normal + paga_extra
    


print("\nCalculo completo ")
print(f"{nombre} trabajo {horas} horas, a una paga de {paga_hora} pesos por hora")
print(f"Paga normal            : $ {paga_normal:13,.2f}")
print(f"Paga extra             : $ {paga_extra:13,.2f}")
print(f"Total                  : $ {total:13,.2f}")