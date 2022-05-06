# # Cree un script que le solicite al usuario leer un número entero entre 1 y 100 en el intervalo (1,100]. El
# # programa debe ser capaz de solicitarle al usuario que reingrese el número
# # cuantas veces sea necesario, hasta que el usuario provea un dato válido. Cada
# # vez que detecte un error de validación, informele al usuario cuál fue el error, con
# # los mensajes “El dato ingresado no es numérico.”, o “El número ingresado está
# # fuera del rango permitido.”. Finalmente, cuando el usuario ingrese un dato
# # válido, muestre el mensaje “[NÚMERO] es válido. Gracias!”.

# def leer_numero():
#     return input('Ingrese un número entre 1 y 100: ')


# def validar_num(num):
#     resultado = True
#     if not num.isdigit():
#         resultado = False
#         print("El valor ingresado no es un numero")
#     elif int(num) < 1 or int(num) > 100:
#         resultado = False
#         print("El valor ingresado está fuera del rango")
        
#     return resultado


# def num_ingresado():
#     numero = leer_numero()
#     while not validar_num(numero):        
#         numero = leer_numero()
#     print(f"{numero} es válido. Gracias!")

# num_ingresado()


# def valido():
#     centinela = True
#     while centinela:
#         numero = input("Ingrese un numero entre el 1 y el 100:")
#         if numero.isdigit():
#             if 0 < int(numero) and int(numero) <= 100:
#              print(f"{numero} es valido. Gracias!")
#              centinela = False
#             else:
#              print("El numero ingresado esta fuera del rango permitido.")
#         else:
#             print("El dato ingresado no es numerico.")
            
# valido()

numeros = 0


while numeros != "listo":
    numeros = (input (f"ingrese un numero del 1 al 100"))
   
    if  not numeros.isdigit():
        print (f" el dato ingresado no es numerico ")
        


    elif int (numeros) >= 0 and int (numeros) <= 100:
         print (f"{numeros} es valaaaido. Gracias ") 
         numeros = "listo"

    elif int(numeros) <0 or int(numeros) > 100:
        print (f"El número ingresado está fuera del rango permitido. Ingrese un numero valido")