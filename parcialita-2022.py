# Consigna 1: ¿Cuál es el mínimo y máximo de iteraciones de un programa que procesa 
# los precios de 200 libros, si debe verificar que 
# al menos 5 de los libros cuesten más que 500 pesos? Justifique de manera breve y concisa.


# Consigna 2: Escriba una función en Python que permita procesar 
# la información sobre n webinars (charlas online).
#  La función recibirá como parámetro la cantidad de webinars que deben ser procesados (n).
# Por cada webinar, el programa debe solicitar ingresar el título de la actividad 
# y el número de inscriptos. Por ejemplo, una entrada válida del
#  programa sería el valor 77 para el número de inscriptos e 
# “Introducción a Redes Neuronales” para el título.
# Una vez procesados todos los webinars, el programa debe informar:
# El título del webinar con la mayor cantidad de inscriptos.
# El promedio de inscriptos entre todos los webinars.

# Consigna 3: Escriba una función en Python que reciba como parámetros dos números 
# naturales n y m, donde n < m, (no hace falta validar) y 
# retorne el producto de todos los números entre n y m ellos incluidos. Ejemplo, n=2, m=4, resultado=2*3*4=24

# Consigna 2

def calcular_webinars(n):

    contador = 0
    promedio = 0
    titulo = ""
    maximo_inscriptos = 0

    for x in range(1,n+1):
        nombre = input("Ingrese el titulo del webinar")
        cantidad = int (input("inscriptos"))
        if cantidad > maximo_inscriptos:
            maximo_inscriptos = cantidad
            titulo = nombre
            
        contador += cantidad
    promedio = contador/n



def producto(n,m):
    producto = 1
    for x in range(n,m+1):
        producto *=  x

    return producto


