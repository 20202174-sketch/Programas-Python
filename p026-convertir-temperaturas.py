#p026-convertir-temperaturas
#Convertir temperaturas de grados Celsius a Farenheit y viceversa

print("\033[2J\033[H")
print("\033[31mConvertir de Grados Celsius a Grados Farenheit\033[0m")

print("\033[34m")
print("[C] elcius a Farenheit")
print("[F] arenheit a Celsius")
print("\033[0m")
op = input("Elige ? ").upper()


if op=="C":
    print("\nConvirtiendo de celsius a Farenheit")
    c = float(input("Introduce los grados Celsius"))
    f = ( c * 9 / 5) + 32
    print(f"\n{c:.2f} grados Celsius, equivale a {f:.2f} grados Farenheit")
else:
    if op=="F":
        print("\nConvirtiendo de Farenheit a Celsius")
        f = float(input("Introduce los grados Farenheit ?"))
        c = (f - 32) * 5 / 9
        print(f"\n{f:.2f} grados Farenheit, equivale a {c:.2f} grados Centigrados")
    else:
        print("Opcion invalida!!")