# p011-operadores-asignacion
# Demostrar el uso de los operadores de asignación

print("="*40)
print("Operadores de Asignación en Python")
print("="*40)

#Operador de asignación básico (=)
#x=float(input("ingresa un número: {x}"))
x=10
print(f"Valor inicial de x: {x}")

x += 5
print(f"x += 5 → x = {x}") #Equivale a x = x + 5
x -= 3
print(f"x -= 3 → x = {x}") # Equivale a: x = x - 3
x *= 2
print(f"x *= 2 → x = {x}") # Equivale a: x = x * 2
x /= 4
print(f"x /= 4 → x = {x}") # Equivale a: x = x / 4
x %= 3
print(f"x %= 3 → x = {x}") # Equivale a: x = x % 3
x **= 2
print(f"x **= 2 → x = {x}") # Equivale a: x = x ** 2
x //= 2
print(f"x //= 2 → x = {x}") # Equivale a: x = x // 2