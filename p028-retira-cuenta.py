#p028-retira-cuenta
#Simula el retiro de dinero de una cuena de ahorros revisa el saldo

saldo_actual = 15000.00
print("Simulacro de retiro ")
print("\033[2J\033[H")
print(f"Tu saldo inicial es de {saldo_actual:.2f}")

cantidad_retiro = float(input("Cantidad a retirar : $ "))

if cantidad_retiro > 0:
    #print("Procediendo con el retiro ..")
    if cantidad_retiro <= saldo_actual:
        saldo_actual -= cantidad_retiro
        print("\nRetiro Exitoso")
        print(f"tu nuevo saldo es : {saldo_actual:.2f}")
    else:
        print("\nLa cantidad a retirar debe ser una cantidad menor a tu saldo inicial")
    print("\nProceso terminado")