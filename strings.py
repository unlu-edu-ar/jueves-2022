#Escribir una función que reciba una cadena que contiene un largo número entero 
# y devuelva una cadena con el número y las separaciones de miles. 
# Por ejemplo, si recibe '1234567890', debe devolver '1.234.567.890'.

def agregar_puntos(numero):
    resultado = ''
    for i, letra in enumerate(numero[::-1]):
        if i % 3 == 0 and i != 0:
            resultado += '.'+ letra
        else:
            resultado += letra
    return resultado[::-1]

def agregar_puntos2(numero):
    resultado = ''
    for i in range(len(numero)-1,-1, -1):
        print(i, numero[i], len(numero) - i)
        if (len(numero) - i) % 3 == 0 and (len(numero) - i) != 0:
            resultado = '.' + numero[i] + resultado
        else:
            resultado =  numero[i] + resultado
    return resultado
     
def agregar_puntos3(numero):
    resultado = ''
    i = 0
    otro_numero = ''
    for letra in numero:
        otro_numero = letra + otro_numero
    
    numero = otro_numero
    for letra in numero:
        print(letra)
        if i % 3 == 0 and i != 0:
            resultado =  letra + '.' + resultado
        else:
            resultado = letra + resultado
        i += 1
    return resultado


def agregar_puntos4(numero):
    resultado = ''
    cantidad_numeros = len(numero)
    for i in range(cantidad_numeros):
        nuevo_indice = cantidad_numeros - 1 - i 
        if i % 3 == 0 and i != 0:
            resultado = numero[nuevo_indice] + '.' + resultado
        else:
            resultado = numero[nuevo_indice] + resultado

    return resultado

print(agregar_puntos4('1234567890'))