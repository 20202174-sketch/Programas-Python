#p004-paga-trabajador
#calcula la paga de un trabajador

print("Calculando la paga de un trabajador \n")

nombre = input ("Nombre : ")
horas = int ( input("Horas : "))
paga = float ( input("paga x hora"))

#Proceso
tasa = 0.03
pagabruta = horas * paga
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto
#Salida
print("\nResumen de pagos ")
print(f"El trabajador {nombre}, trabajo {horas} horas, con una paga de {paga:,.2f} pesos, con una tasa de {tasa:.2f}")
print(f"pagabruta       :{pagabruta:,.2f}")
print(f"Impuesto         :{impuesto:,.2f}")
print(f"Paga neta        :{paganeta:,.2f}")