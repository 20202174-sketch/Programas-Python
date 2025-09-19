# p013-funciones-matematicas-precios
# Demostrar el uso de funciones matemáticas para redondeo y manejo de precios

import math as gabo # el "as gabo" es para no escribir math asi lo remplazo con lo que yo quiera en este caso gabo, pero tambien puede ser mt, gp, o cualquier otra varaiable que no sea una palabra reservada

#Precio con decimales
precio = 15.65

#Diferentes metodos de redondeo
arriba = gabo.ceil(precio)
abajo = gabo.floor(precio)
truncado = gabo.trunc(precio)
redondeo = round(precio)
un_decimal = round(precio,1)

# Mostrar resultados con formato
print(f"Precio original.: {precio}")
print(f"Precio Arriba.: {arriba}")
print(f"Precio Abajo.: {abajo}")
print(f"Precio Truncado.: {truncado}")
print(f"Precio Redondeado.: {redondeo}")
print(f"Precio con un Decimal.: {un_decimal}")
