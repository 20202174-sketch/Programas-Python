# p122-operaciones-conjuntos.py
# Operaciones entre conjuntos

c1 = {1, 2, 3, 4, 5}
c2 = {5, 6, 7, 8, 9, 10}
c3 = {9, 10, 11, 12, 13}
c4 = {3, 4, 5}

print('\033[H\033[J')

print("Conjuntos Base")
print(f"c1: {c1}\nc2: {c2}\nc3: {c3}\nc4: {c4}")

print("\nUnion ( | )")
print(f"c1 union c2: {c1.union(c2)}") #metodo1
print(f"c1 union c3: {c1 | c3}") #metodo 2

print("\nIntersección ( & )")
print(f"c1 intersección c2: {c1.intersection(c2)}") #metodo1
print(f"c2 intersección c3: {c2 & c3}") #metodo 2

print("\nDiferencia ( - )")
print(f"c1 diferencia c4 (Elementos en c1, no en c4): {c1.difference(c4)}") #metodo 1
print(f"c2 diferencia c3 (Elementos en c2, no en c3): {c2 - c3}") #metodo 2

print("\nDiferencia Simétrica ( ^ )")
print(f"c1 dif. simétrica c2 (Elementos en c1 o c2, no en ambos):{c1.symmetric_difference(c2)}")#metodo 1
print(f"c2 dif. simétrica c3: {c2 ^ c3}")#metodo 2

print("\nSubconjuntos ( <= )")
print(f"¿c4 es subconjunto de c1? : {c4.issubset(c1)} (True)") #metodo 1
print(f"¿c3 es subconjunto de c2? : {c3 <= c2} (False)") #metodo 2

print("\nSuperconjuntos ( >= )")
print(f"¿c1 es superconjunto de c4? : {c1.issuperset(c4)} (True)") #metodo 1
print(f"¿c2 es superconjunto de c3? : {c2 >= c3} (False)") #metodo 2

print("\nPertenece o no pertenece a un conjunto ( in / not in )")
print(f"¿Está el 2 en c1? : {2 in c1} (True)") 
print(f"¿No está el 6 en c1? : {6 not in c1} (True)")