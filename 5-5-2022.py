# Codifique un programa que le solicite al usuario ingresar números enteros, 
# y que vaya mostrando el resultado de multiplicar por 2 cada uno. 
# El programa debe terminar cuando el usuario ingresa el valor especial -1.

# Extienda su solución para que, antes de terminar, 
# el programa muestre en pantalla la suma total de todos los valores ingresados.

# Extienda su solución para que, antes de terminar, 
# el programa muestre en pantalla el promedio de entre todos los valores ingresados.

suma_total = 0
cantidad_numeros = 0

valor_ingresado = 0
while valor_ingresado != -1:
    valor_ingresado = int(input("Ingrese un número entero: "))
    valor_a_mostrar = valor_ingresado * 2
    suma_total += valor_ingresado
    cantidad_numeros += 1
    #suma_total = suma_total + valor_ingresado
    print(valor_a_mostrar)
    
print("La suma total es: ", suma_total)
print("El promedio es: ", suma_total/cantidad_numeros)
    
print("salio del while")