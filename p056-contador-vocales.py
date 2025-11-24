# p056-contador-vocales.py
# Cuenta las vocales y consonantes en una frase y otros caracteres

while True:
    print('\033[H\033[J')
    print("Contador de Vocales y Consonantes")
    frase = input("\nIntroduce una frase: ").lower()
    vocales = consonantes = otros = 0
    indice = 0
    while indice < len(frase):
        caracter = frase[indice] #tomamos el caracter correspondiente de la frase
    # Verificar si es una letra del alfabeto
    if caracter >= 'a' and caracter <='z': # verificamos que sea letra
        if caracter in "aeiou": # es vocal
            vocales += 1
        else: #es consonante
            consonantes += 1
    else: #es cualquier otra cosa
        otros += 1 

    indice += 1 #me paso al siguiente caracter

    print(f"\nAnálisis de la frase:")
    print(f"Número de vocales: {vocales}")
    print(f"Número de consonantes: {consonantes}")
    print(f"Número de caracteres no alfabéticos: {otros}")
    if input('\n¿Deseas analizar otra frase (S/N)? ').upper() == 'N':
        break