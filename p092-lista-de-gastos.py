#092-lista-de-gastos
#Permite llevar el control de una lista de gastos

print('\033[H\033[J')

gastos = [450.50, 120.00, 85.90, 230.00, 55.75]
limite_gastos = 100.00

while True:
    print("\n---Menu de gestion de gastos---")
    print("1. Ver todos los gastos")
    print("2. Agregar un nuevo gasto")
    print("3. Modificar un gasto existente")
    print("4. Eliminar un gasto (por reembolso o error)")
    print("5. Ver resumen y total de gastos")
    print("6. Salir")
    opcion = int(input('Elige una opcion (1-6) :'))

    if opcion == 1: #Ver los gastos
        print("\n--- Tus gastos Registrados---")
        print(gastos)
    elif opcion == 2: #Agregar gastos
        try: 
            nuevo_gasto = float(input("Ingresa el monto del nuevo gasto: "))
            gastos.append(nuevo_gasto)
            print(f"Gasto de ${nuevo_gasto:.2f} agregado correctamente.")
        except ValueError:
            print("Error: Porfavor, ingresa un numero valido")
    elif opcion == 3: #Modificar gastos
        try:
            pos = int(input("Ingresa la posicion en la lista del gasto que quieres modificar: "))
            valor_anterior = gastos[pos]
            print(f"Gastos a modificar gastos[{pos}] ${valor_anterior:.2f}")
            nuevo_valor = float(input("Ingresa el monto del gasto"))
            gastos[pos] = nuevo_valor
            print(f"Gasto modificado de ${valor_anterior:.2f} a ${nuevo_valor:.2f}.")
        except IndexError:
            print("Error: La posicionespecificada no se encuentra en la lista.")
        except ValueError:
            print("Error: Por favor, ingresa numeros validos.")
    elif opcion == 4:
        try:
            gastos_a_eliminar = float(input("Ingresa el monto del gasto que quieres eliminar: "))
            if gastos_a_eliminar in gastos:
                gastos.remove(gastos_a_eliminar)
                print(f"Gasto de ${gastos_a_eliminar:.2f} eliminado correctamente.")
            else:
                print("Error: El gasto especificado no se encuentra en la lista.")
            
        except ValueError:
            print("Error: Porfavor, ingresa un numero valido.")
    elif opcion == 5:
        if not gastos:
            print("\nNo hay gastos para mostrar.")
        else:
            total_gastado = 0
            print("\n---Resumen del Mes ---")
            for gasto in gastos:
                total_gastado += gasto
                if gasto > limite_gastos:
                    print(f"Gasto considerable detectado: ${gasto:.2f}")
            print(f"\nEl gasto total del mes es: ${total_gastado:.2f}")
    elif opcion == 6:
        print("\nGracias por usar el gestor de gastos. ¡Hasta pronto!") 
        break
    else:
        print("Opcion no valida. Porfavor, elige un numero del 1 al 6.")