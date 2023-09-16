def contar_letras_a(cadena):
    cadena = cadena.lower()
    contador = 0

    for letra in cadena:
        if letra == 'a':
            contador += 1

    return contador
cadena = input("Ingrese una cadena de texto: ")

cantidad_a = contar_letras_a(cadena)

print("La cantidad de letras 'a' o 'A' en la cadena es: ", cantidad_a)	
