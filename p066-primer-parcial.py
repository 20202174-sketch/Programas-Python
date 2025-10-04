"""
Objetivo: [Escribe aqui el objetivo del programa]
Nombre del Alumno: [Gabriel Rodriguez Sustaita]
Matrícula: [20202174]
Materia: Computación Aplicada
Examen: Primer Parcial
"""

# --- Inicialización de Contadores y Acumuladores ---
# Aquí se declaran todas las variables que necesitarás para guardar los datos

# --- Contadores de Asistentes ---
total_estudiantes = 0
total_adultos = 0
total_tercera_edad= 0
total_academicos = 0

# ... (agrega los demás contadores de tipo de comprador y de sexo)
total_hombres = 0
total_mujeres = 0

total_asistentes = 0
total_rechazados = 0
suma_edades = 0

# --- Acumuladores de Ingresos ---
ingresos_estudiantes = 0.0
ingresos_adultos = 0.0
ingresos_tercera_edad = 0.0
ingresos_academicos = 0.0
# ... (agrega los demás acumuladores de ingresos)
ingresos_totales = 0.0
# --- Precios de los Boletos (constantes) ---
PRECIO_ESTUDIANTE = 50.0
PRECIO_ADULTO = 90.0
# ... (agrega las demás constantes de precios)
PRECIO_TERCERA_EDAD = 60.0
PRECIO_ACADEMICO = 70.0

print('\033[2J\033[H')
print("--- Sistema de Venta de Boletos de Cine ---")

# --- Ciclo Principal para la Venta de Boletos ---
# Usaremos un ciclo while para registrar ventas hasta que el usuario decida parar.
continuar_venta = "s"
while continuar_venta == "s":

    print("\n--- Nueva Venta ---")
    # --- 1. Solicitud de Datos ---
    # Pide la edad, el tipo de comprador y el sexo.
    # ¡Recuerda convertir la edad a un número entero!
    
    edad = int(input("Introduce la edad del comprador: "))
    # ... (pide el tipo de comprador y el sexo)
    print("Tipos de comprador: [E]studiante, [A]dulto, [T]ercera edad, [C]adémico")
    tipo = input("Tipo de comprador (E/A/T/C): ")
    # ... (Ayuda a mostrar "Estudiante, Adulto, etc.. en vez de ue solo muestre la inicial")
    if tipo == "E" or tipo == "e":
        tipop = "Estudiante"
    elif tipo == "A" or tipo == "a":
        tipop = "Adulto"
    elif tipo == "T" or tipo == "t":
        tipop = "Tercera Edad"
    elif tipo == "C" or tipo == "c":
        tipop = "Academico"
    else:
        tipop = "DATO NO RECONOCIDO"
        
    sexo = input("Sexo (H=Hombre / M=Mujer): ")
    if sexo == "H" or sexo == "h":
        sexop = "Hombre"
    elif sexo == "M" or sexo == "m":
        sexop = "Mujer"
    else:
        sexop = "DATO NO RECONOCIDO"

    # --- 2. Validación de Edad (Clasificación B) ---
    # La película es para mayores de 13 años.
    
    if edad > 13:
        # Si la edad es permitida, procede con la venta.
        # Muestra el mensaje de bienvenida con los datos registrados
        # agregue este if y elif para poner bienvenido o bienvenida dependiendo el sexo

        if sexop == "Hombre":
            print(f"¡Bienvenido!... edad: {edad}, tipo de comprador: {tipop}, sexo: {sexop} ..")
        elif sexop == "Mujer":
            print(f"¡Bienvenida!... edad: {edad}, tipo de comprador: {tipop}, sexo: {sexop} ..")

        
        
        # --- 3. Actualización de Estadísticas Generales ---
        # Incrementa el contador de asistentes y suma la edad para el promedio.
        # Incrementa el contador de sexo correspondiente (hombre o mujer).

        total_asistentes = total_asistentes + 1
        suma_edades = suma_edades + edad

        if sexo == "H" or sexo == "h":
            total_hombres = total_hombres + 1
        else:
            total_mujeres = total_mujeres + 1

        # --- 4. Cálculo de Costo y Actualización de Contadores Específicos ---
        # Usa una estructura if/elif/else para determinar el precio y actualizar
        # los contadores del tipo de comprador y sus ingresos.
        # Suma el costo del boleto a los ingresos totales.
        costo = 0.0

        if tipo == "E" or tipo == "e":
            costo = PRECIO_ESTUDIANTE
            total_estudiantes = total_estudiantes + 1
            ingresos_estudiantes = ingresos_estudiantes + costo
        elif tipo == "A" or tipo == "a":
            costo = PRECIO_ADULTO
            total_adultos = total_adultos + 1
            ingresos_adultos = ingresos_adultos + costo
        elif tipo == "T" or tipo == "t":
            costo = PRECIO_TERCERA_EDAD
            total_tercera_edad = total_tercera_edad + 1
            ingresos_tercera_edad = ingresos_tercera_edad + costo
        else:
            costo = PRECIO_ACADEMICO
            total_academicos = total_academicos + 1
            ingresos_academicos = ingresos_academicos + costo

        ingresos_totales = ingresos_totales + costo

    else:
        # Si la edad no es permitida, muestra un mensaje y actualiza el contador ()
        print("ACCESO DENEGADO: El comprador es menor de 13 años.")
        # ... (incrementa el contador de personas rechazadas)
        total_rechazados = total_rechazados + 1

    # Pregunta al usuario si desea registrar otra venta.
    continuar_venta = input("\n¿Deseas registrar otra venta? (S/N): ").lower()

# --- FIN DEL CICLO ---

# --- 5. Cálculo de Promedio ---
# Calcula el promedio de edad. Cuidado con la división entre cero si no hubo asistentes.
promedio_edad = 0
# if total_asistentes > 0:
#     promedio_edad = ... # (calcula el promedio aquí)
if total_asistentes > 0:
    promedio_edad = suma_edades / total_asistentes


# --- 6. Impresión del Reporte Final ---
print("\n*** REPORTE FINAL DE LA FUNCIÓN ***")

print("\n--- Estadísticas del Público ---")
# Imprime todos los totales de asistentes por tipo y sexo.
print("Total de Estudiantes:", total_estudiantes)
print("Total de Adultos:", total_adultos)
print("Total de Tercera Edad:", total_tercera_edad)
print("Total de Académicos:", total_academicos)

print("Total de Hombres:", total_hombres)
print("Total de Mujeres:", total_mujeres)

print("Total de Asistentes a la Funcion:", total_asistentes)
print("Promedio de edad de todos los asistentes: %.2f" % promedio_edad)
print("Total de Personas rechazadas por la edad:", total_rechazados)

print("\n--- Reporte de Ingresos ---")
# Imprime todos los ingresos por tipo de comprador y el total general.
# Utiliza formato para mostrar dos decimales en el dinero.
print("Total de dinero recaudado por Estudiantes: $%.2f" % ingresos_estudiantes)
print("Total de dinero recaudado por Adultos: $%.2f" % ingresos_adultos)
print("Total de dinero recaudado por Tercera Edad: $%.2f" % ingresos_tercera_edad)
print("Total de dinero recaudado por Académicos: $%.2f" % ingresos_academicos)
print("Total de dinero recaudado en general. $%.2f" % ingresos_totales)

print("\n--- Rentabilidad ---")
# --- 7. Mensaje de Rentabilidad ---
# Usa una estructura if/elif/else para determinar si las ganancias
# fueron BAJAS, MODERADAS o BUENAS, basándote en los ingresos totales.
if ingresos_totales < 1500:
    print("La función generó BAJAS ganancias.")
elif ingresos_totales <= 3500:
    print("La función generó ganancias MODERADAS.")
else:
    print("La función generó BUENAS ganancias.")


"""
Preguntas: Explica con tus palabras

1. Imagina que el cine decide implementar una promoción: los martes, todos los boletos de Adulto tendrán un 20% de descuento. 
¿Qué cambios tendrías que hacer en tu código para agregar esta funcionalidad? 
Menciona qué nueva pregunta le harías al usuario y en qué parte del código agregarías la nueva lógica.

[tendria que agregar los dias de la semana para que el programa sepa cuando es martes, ya sea que la ponga en tiempo 
real o que ponga el dia manualmente cuando inicie el programa, despues en tendria que pner un if en donde se selecciona 
lo de adulto si selecciona adulto entrar a un if donde checa si es martes y si asi lo es, le aplica una descuento al precio. 
con respecto a la pregunta no la veo muy necesria pero anidaria un if en que acabao de mencionar donde el usuario se le pregunte
tienes un descuento del 20% lo quieres aplicar si o no, y dependiendo de la respuesta se salta ese paso y corre todo igual o si
entrara a la opcion de aplicar el descuento entraraia al if dond esta la operacion para aplicarlo; creo que lo mas recomendado
es poner solo un comentario donde dice bienvenido o bienvenida diciendo: "Tienes un descuento del 20%" y mstrar el precio real y el precio de descuento]

2. Supongamos que, al probar tu programa, el "Total Recaudado en General" siempre te da un resultado incorrecto, 
aunque los ingresos por cada tipo de comprador parecen correctos. 
Describe, paso a paso, qué harías para encontrar el error. 
¿En qué líneas específicas de tu código pondrías atención para verificar los valores y solucionar el problema?

primero checaria desde donde se generan las variables que todas inicien en cero 
despues checaria que todos los nombres sean los mismos
posteriormente checaria donde puse los costos en las variables que esten bien y checar los nombres, de hay me pasaria a las linea 108-127
y haria pruebas linea por linea que me de lo que corresponda, realizando esas pruebas con multipes valores para descartar exponteneidad o algo similar,
si todo esta bien ya solo me pasaria a ver donde se estan imprimiendo que este imprimiendo lo correcto

creo que en este codigo yo checaria desde la linea 108-127 las cuales considero son las mas importantes y la linea del print line 173 

"""
