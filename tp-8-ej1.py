# Cree un script que le pida al usuario ingresar palabras, una a una, hasta que el
# usuario ingrese la palabra “parar”. A medida que se van ingresando las palabras,
# el programa simplemente debe mostrarlas en pantalla. Al detectar la palabra
# para detenerse, debe mostrar el mensaje “--- TERMINADO ---”.


# palabra_adivinar = "COCHE"
# palabra = input("ingrese na palabra si esa palabra es PARAR el programa parara")
# intentos = 0
# while palabra != palabra_adivinar and intentos < 4:
#     print(palabra)    
#     palabra = input("ingrese na palabra si esa palabra es PARAR el programa parara")
#     intentos += 1
# if intentos< 4:
#     print("GANASTE")
# else:
#     print("“--- TERMINADO ---”")

def mostrar_palabra(letra, palabra_adivinar,adivinado):
    respuesta = ""
    for l in range(len(palabra_adivinar)):
        if palabra_adivinar[l] == letra:
            respuesta += palabra_adivinar[l]
        else:
            respuesta += adivinado[l]
            
    return respuesta


palabra_adivinar = "COCHE"
palabra = ""
intentos = 0
adivinado = "______"
while palabra != palabra_adivinar and intentos < 5:
    print(f"te quedan {5 - intentos} intentos")
    letra_palabra = input("ingrese letra o la palabra entera")

    if len(letra_palabra) > 1:
        palabra = letra_palabra
        adivinado = palabra
    else:
        palabra = mostrar_palabra(letra_palabra, palabra_adivinar,adivinado)
        adivinado = palabra
        palabra = adivinado
        print("adivinaste",palabra)
    intentos+=1

if adivinado == palabra_adivinar:
    print("GANASTE")
else:
    print("PERDISTE")




