# Codifique un programa que le solicite al usuario ingresar su nombre de pila y edad. 
# En ambos casos se debe verificar que la entrada es válida, y en caso de no serlo, 
# se le debe permitir reingresar el dato en cuestión, o abortar el programa (a elección del usuario).

# El nombre de pila debe ser un valor alfanumérico que contenga sólo letras (no se admiten números).

# La edad debe ser un valor numérico mayor a 18 y menor a 99.

# Cuando se obtengan los dos valores correctamente, el programa debe simplemente saludar al usuario mostrando su nombre y edad.

# validado = True
# contador = 0

# while not validado and contador < 2:
#     contador += 1
#     nombre = input('Ingrese su nombre de pila: ')
#     edad = input('Ingrese su edad: ')
    
#     if nombre.isalpha() and edad.isdigit() and int(edad) > 18 and int(edad) < 99:
#         validado = True
#         print(f"Hola {nombre}, tu edad es {edad}.") 
#     elif contador < 2:
#         eleccion = input("Datos invalidos. Desea volver a ingresarlos? Para continuar escriba si. ")
#         if eleccion != 'si':
#             validado = True
eleccion = True

while eleccion:
    entrada = input("Ingrese si desea continuar o no: ")
    if entrada.isdigit():
        eleccion = False
    

    
        

    





