# Escriba un algoritmo que, conociendo las notas de los dos parciales de un
# alumno de la asignatura Introducción a la Programación, muestre en
# pantalla su promedio.

def promedio(nota1, nota2):
    promedio = (nota1 + nota2) // 2
    return promedio
    
# parcial1 = int(input("Nota del primer parcial "))
# parcial2 = int(input("Nota del segundo parcial "))

# print(promedio(parcial1, parcial2))

def test_promedio():
    print("Testeando la función promedio...")
    assert promedio(8,6) == 7
    assert promedio(0,0) == 0
    print("Pasó!!!")
    
#test_promedio()


def contar_nombre(x):
    nombre = len(x)
    return nombre

def test_contar_nombre():
    print("Testeando la función contar_nombre...")
    assert contar_nombre("mario") == 5
    assert contar_nombre("") == 0
    assert contar_nombre("10") == 10
    print("Pasó!!!")

test_contar_nombre()

# nombre1 = input("ingrese un nombre:")
# print(f"El nombre {nombre1} tiene {contar_nombre(nombre1)} letras.")
# print(contar_nombre(nombre1))