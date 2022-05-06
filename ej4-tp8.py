# Construya un menú que le muestre al usuario lo siguiente:
# ********* MI PROGRAMA *********
# 1. Saludar.
# 2. Informar temperatura.
# 3. Mostrar nombre de materia.
# 4. Salir.
# Seleccione una opción [1-4]:
# ● - Cuando el usuario ingrese la opción 1, se mostrará el mensaje:
# “Hola, bienvenido a mi programa interactivo!”.
# ● - Cuando el usuario ingrese la opción 2, se mostrará el mensaje
# “Hay una sensación térmica de 20 grados Celsius.”.
# ● - Cuando el usuario ingrese la opción 3, se mostrará el mensaje
# “Estás en la materia Introducción a la Programación!”.
# ● - Cuando el usuario ingrese la opción 4, el programa debe terminar,
# mostrando el mensaje “Hasta la próxima!”.
# ● - Si el usuario ingresa una opción inválida, se muestra el mensaje “Opción
# inválida.”.

# Tip 1: crear al menos una función propia, que se encargue exclusivamente
# de mostrar el menú de opciones en pantalla.
# Tip 2: puede utilizar la instrucción os.system('cls') para limpiar la
# pantalla antes de volver a mostrar el menú. De esta manera su programa
# será más legible en la terminal. Para poder utilizar dicha instrucción
# deberá importar, al principio del script, la librería os de la siguiente
# manera:

import os
# # su código

# Tip 3: antes de limpiar la pantalla y volver a mostrar el menú, puede
# esperar a que el usuario confirme que ha terminado de leer la información
# presentada, simplemente utilizando la función
# input(‘PRESIONE ENTER PARA CONTINUAR’).

def menu():
    print("********* MI PROGRAMA *********")
    print("1. Saludar.")
    print("2. Informar temperatura.")
    print("3. Mostrar nombre de materia.")
    print("4. Salir.")
    
ingresado = ""
while ingresado != "4":
    #os.system('clear')
    menu()
    ingresado = input("Seleccione una opción [1-4]: ")
    if ingresado == "1":
        print("Hola, bienvenido a mi programa interactivo!")
    elif ingresado == "2":
        print("Hay una sensación térmica de 20 grados Celsius.")
    elif ingresado == "3":
        print("Estás en la materia Introducción a la Programación!")
    elif ingresado == "4":
        print("Hasta la próxima!")
    else:
        print("Opción inválida")
        
    input("PRESIONE ENTER PARA CONTINUAR")