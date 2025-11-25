# p130-func-param-defecto.py

def calcular_total(monto: float, iva: float = 0.16) -> float:

    return monto + (monto * iva)

res = calcular_total(1000)
print(f"Total 1: ${res:,.2f}")

print(f"Total 2: ${calcular_total(1000, 0.08):,.2f}")