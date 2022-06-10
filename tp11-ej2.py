# Dada una lista de números enteros, escribir una función para cada uno de los
# siguientes ítems:
# a- Devuelva una lista con todos los números que sean primos.
# b- Devuelva la sumatoria y el promedio de los valores.
# c- Devuelva una lista con el factorial de cada uno de esos números.

def es_primo(numero):
    cantidad = 0
    for i in range(1,numero+1):
        if numero % i == 0:
            cantidad += 1

    return cantidad == 2

def factorial(numero):
    fact = 1
    for n in range(1,numero+1):
        fact *=  n
    return fact


def lista_de_primos(lista):
    lista_primos=[]
    for numero in lista:
        if es_primo(numero):
            lista_primos.append(numero)
    return lista_primos


def sumatoria(lista):
    sum = 0
    prom =0
    for i in lista:
        sum += i
    prom = sum/len(lista)
    return sum , prom


def lista_factoriales(lista):
    lista_de_factoriales=[]
    for i in lista:
        aux = factorial(i)
        lista_de_factoriales.append(aux)
    return lista_de_factoriales


lista = [3,2,4]

print(lista_de_primos(lista))            
print(sumatoria(lista))            
print(lista_factoriales(lista))
