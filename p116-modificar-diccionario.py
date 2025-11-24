# p116-modificar-diccionario.py
# • Crea un diccionario llamado paises con los siguientes pares (llave: valor): Argentina: 100, Brasil: 200,
# Colombia: 300, Chile: 400, Ecuador: 500, Bolivia: 600, Jamaica: 700.
# • Muestra el diccionario inicial.
# • Modifica los valores de las siguientes llaves:
# o Cambia el valor de Brasil a 250 (usando []).
# o Cambia el valor de Chile a 450 (usando []).
# o Cambia el valor de Bolivia a 650 (usando update()).
# o Cambia el valor de Jamaica a 750 (usando update()).
# • Muestra el diccionario modificado.

print('\033[H\033[J')
print("Modificación de valores en un diccionario\n")

paises = {
    "Argentina": 100,
    "Brasil": 200,
    "Colombia": 300,
    "Chile": 400,
    "Ecuador": 500,
    "Bolivia": 600,
    "Jamaica": 700
}

# Mostrar diccionario original
print("Diccionario inicial:")
print(paises, "-", len(paises), "\n")

# Cambios solicitados
paises["Brasil"] = 250       # usando []
paises["Chile"] = 450        # usando []
paises.update({"Bolivia": 650})   # usando update()
paises.update({"Jamaica": 750})   # usando update()

# Mostrar resultado final
print("Diccionario modificado:")
print(paises, "-", len(paises))
