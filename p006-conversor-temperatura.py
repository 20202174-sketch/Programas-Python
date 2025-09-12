#p006-conversor-temperatura.py
#convierte temperatura de celsius a farenheit

print("Conversor de Temperatura (Celcius - Farenheit)\n")

celcius = float ( input("Ingresa la Temperatura en Celsius : "))

farenheit = (celcius * 9/5) +32

print(f"{celcius:.2f} grados celsius equivale a {farenheit:.2f} farenheit")