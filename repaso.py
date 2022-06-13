# Escribir una función que reciba una cadena a buscar y una lista de nombres
# de personas y busque dentro de la lista, todas los elementos que contengan esa
# cadena o cualquier parte de ella. Debe devolver una lista con los elementos
# encontrados.

# def buscar_nombre(cadena, lista): 
#     elem_encontrados = [] 
#     for i in lista:
#         if cadena in i: 
#             elem_encontrados.append(i) 
#     return elem_encontrados 

# print(buscar_nombre('auto', ['a', 'auto', 'automatizar', 'automatico', 'pauto', 'pepe'])) 



# Cree un script que le solicite al usuario ingresar una temperatura en grados Celsius, y 
# valide que la entrada es correcta, teniendo en cuenta que la temperatura debe ser un valor numérico, y 
# el rango válido está entre -18 y 50. El programa debe permitir reingresar el dato cuantas veces sea necesario, 
# hasta que el usuario provea un dato válido. Procure informar al usuario cuando su dato es inválido, y
#  cuáles son los valores aceptados. 

# temperatura = input("Ingrese una temperatura:")
# while not(not temperatura.isalpha()) and int(temperatura) >= -18 and int(temperatura) <= 50:
#     temperatura = input('La temperatura es invalida, Ingrese nuevamente una temperatura:') 
#     print(f'La temperatura es {temperatura}') 

def temperaturacelsius(): 
    flag = True
    print("La temperatura debe estar entre -18° y 50°, * para cerrar") 
    while flag: 
        temperatura = input("Ingrese la temperatura en grados celsius: ") 
        if not temperatura.isalpha(): 
            temperatura = int(temperatura) 
            if temperatura > -18 and temperatura < 50: 
                print("¡La temperatura ingresada es correcta!") 
                flag = False
            else: 
                print("¡La temperatura ingresada es incorrecta!") 
                # temperatura = input("Ingrese la temperatura en grados celsius: ") 
        else: 
            print("La temperatura ingresada no corresponde a un valor numerico.") 
            # temperatura = input("Ingrese la temperatura en grados celsius: ")     
    
# temperaturacelsius()

# Dada una lista de números enteros y un entero k, escribir una función para
# cada uno de los siguientes ítems:
# a- Devuelva tres listas, una con los menores, otra con los mayores y otra con los
# iguales a k.
# b- Devuelva una lista con aquellos que son múltiplos de k.

def es_multiplo(k,numero):
    return numero % k == 0

def maymen(k,lista):
    lista_mayores = []
    lista_menores = []
    lista_iguales = []
    for elemento in lista:
        if elemento > k:
            lista_mayores.append(elemento)
        elif elemento < k:
            lista_menores.append(elemento)
        else:
            lista_iguales.append(elemento)

    return lista_mayores, lista_menores, lista_iguales

def multiplos(k,lista):
    lista_multiplos = []
    for elemento in lista:
        if es_multiplo(k,elemento):
            lista_multiplos.append(elemento)
    return lista_multiplos


# print(multiplos(3,[3,5,6,7,9,12]))

# Variación: Escriba una función en Python que reciba como parámetro una lista de enteros 
# y muestre por pantalla la sumatoria de todos los números de la lista.
#  E1: [3,7, 1] Muestra 11 E2: [1] Muestra 1 

def sumatoria_promedio(lista):
    suma = 0
    largo = len(lista)
    for i in lista:
        suma = suma + i
    if largo > 0:
        promedio = suma/len(lista)
    else:
        promedio = 0
    return suma, promedio

# range(4) = [0,1,2,3]
def buscar_mayor():
    # mayor=-999999
    # menor=999999
    for i in range(3):
        numero = int(input("ingrese un numero"))
        if i == 0:
            menor = numero 
            mayor = numero

        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero

