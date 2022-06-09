# OBJETIVO DEL EJERCICIO
# Comprender el concepto de Listas  y ejercitar las técnicas básicas en Python para trabajar con ellas.

# ENUNCIADO
# Codifique un programa que le solicite al usuario armar la lista de los legajos inscriptos de Introducción a la Programación. 
# No se sabe cuántos alumnos se van a inscribir, por tanto se recomienda usar un ciclo con centinela.
#  Además tener en cuenta que no haya legajos repetidos.
#  Al final imprimir la lista incluido el orden de inscripción.

# Modificar el programa anterior para permitir ingresar Apellido y Nombre de los inscriptos  y
#  los imprima junto con los legajos.

personas = []
apellidos_nombres = []

fin = False

while not fin:
    persona = int(input("ingrese el legajo o con -1 para terminar "))
    if persona < 0:
        fin = True
    else:
        if persona in personas:
            print(f"el legajo {persona} ya esta inscripto")
        else:
            personas.append(persona)
            apellido_nombre = input("ingrese nombre y apellido")
            apellidos_nombres.append(apellido_nombre)


for indice ,nom_ape in enumerate(apellidos_nombres):
    print(indice,nom_ape)
    print(f"el Legajo {personas[indice]} tiene nombre y apellido {apellidos_nombres[indice]}")
# print(personas)
# print(apellidos_nombres)

