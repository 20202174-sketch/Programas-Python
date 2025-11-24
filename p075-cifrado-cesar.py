# p075-cifrado-cesar.py
# Cifra un mensaje usando el Cifrado Cesar.

while True:
    print('\033[H\033[J')
    print('Cifrando un mensaje usando el Cifrado Cesar')
    mensaje_original = input("Ingresa el mensaje a cifrar: ")
    desplazamiento = int(input("Ingresa la clave de desplazamiento (numero): "))
    mensaje_cifrado = ""

    for caracter in mensaje_original:
        if caracter.isalpha(): 
            codigo_ascii = ord(caracter)
            base = ord('a') if caracter.islower() else ord('A')
            codigo_nuevo = base + (codigo_ascii - base + desplazamiento) % 26
            mensaje_cifrado += chr(codigo_nuevo)
        else:
            mensaje_cifrado += caracter # Los otros caracteres pasan igual

    print(f"\nMensaje Original: {mensaje_original}")
    print(f"Mensaje Cifrado: {mensaje_cifrado}")
    
    if input('\n\n¿Deseas encriptar otro mensaje (S/N)? ').upper() == 'N':
        break

print('\nProceso terminado')