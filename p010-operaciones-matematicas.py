# p010-operaciones-matematicas
# Demostrar el uso de los diferentes operadores aritméticos con números

print("="*50)
print("Calculadora de Operaciones Matematicas")
print("="*50)

#Solicitar numeros al usuario
x=float(input("Ingrese el primer número (x)"))
y=float(input("Ingreze el segundo número (y)"))

print(f"\nResultados con x={x} y y={y}")
print("-"*40)

#Mostrar resultados direcamente con formato alineado
print(f"Suma: {x:>6} + {y:<6} = {x + y:>10.2f}")
print(f"Resta: {x:>6} - {y:<6} = {x - y:>10.2f}")
print(f"Multiplicación: {x:>6} * {y:<6} = {x * y:10.2f}")
print(f"División: {x:>6} ÷ {y:<6} = {x / y:10.2f}")
print(f"Exponenciación: {x:>6} ^ {y:<6} = {x ** y:10.2f}")
print(f"División Entera: {x:>6} // {y:<6} = {x // y:10.2f}")