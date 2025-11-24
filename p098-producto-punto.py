# p098-producto-punto.py
# Cálculo del producto punto de dos vectores

A = [1, 3, -5]
B = [4, -2, -1]
C = 0

print('\033[H\033[J')

print("--- Cálculo del Producto Punto ---\n")
print(f"Vector A: {A}")
print(f"Vector B: {B}\n")

if len(A) == len(B):
    for i in range(len(A)):
        producto = A[i] * B[i]
        C.append(producto)

    print(f"El producto punto de los vectores es: {sum(C)}")
else:
    print("Error: Los vectores deben tener la misma longitud para calcular el producto punto.")