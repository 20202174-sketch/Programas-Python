# p115-acceder-diccionario.py
# • Crea un diccionario llamado dias usando llaves numéricas para los días de la semana.
# • Muestra el diccionario completo.
# • Accede y muestra los siguientes valores específicos:
# o El valor de la llave 1 (usando []).
# o El valor de la llave 7 (usando []).
# o El valor de la llave 5 (usando get()).
# o El valor de la llave 7 (usando get()).
# • Vuelve a mostrar el diccionario completo.

print('\033[H\033[J')
print("Acceso a valores dentro de un diccionario\n")

# Diccionario de días de la semana
dias_semana = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo"
}

# Mostrar diccionario completo
print("Diccionario inicial:")
print(dias_semana, "-", len(dias_semana), "\n")

# Acceder a llaves solicitadas
print("Accediendo a elementos:")
print("Llave 1 (con []):", dias_semana[1])
print("Llave 7 (con []):", dias_semana[7])
print("Llave 5 (con get()):", dias_semana.get(5))
print("Llave 7 (con get()):", dias_semana.get(7))

# Mostrar diccionario otra vez
print("\nDiccionario final:")
print(dias_semana, "-", len(dias_semana))
