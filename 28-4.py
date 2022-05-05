# Codifique un programa que muestre en pantalla los primeros 10 números enteros, 
# comenzando desde el 1. Los números deben mostrarse uno en cada línea.
# Modifique el código para que se muestren sólo los números impares.

# Modifique el código para que se muestren los primeros 10 impares.
#  Modifique el código para que se muestren los primeros x numeros que ingresa el usuario
#  Modifique el código para que se muestren los primeros x numeros PARES que ingresa el usuario
cantidad = int(input("ingrese cuantos impares quiere"))


for numeros in range(0,cantidad*2,2):
    print(f"opcion 1 {numeros}")

# for numeros in range(0,20):
#     if not numeros % 2 == 0:
#         print(f"numero impar {numeros}")


