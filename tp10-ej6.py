#6. Haciendo uso de las funciones para strings que ya conoce, implemente un 
# #script que haga lo siguiente: 
# #I. Le solicite al usuario ingresar una palabra por teclado. Se debe validar que 
# #la palabra tenga al menos una ‘ñ’, que no sea sólo caracteres numéricos, y 
# #que no sean sólo espacios en blanco.
#  En caso de no ser válida, se le debe 
# #pedir al usuario que la reingrese. 
# #II. Informe en pantalla la cantidad de letras de la palabra ingresada.
# #III. Transforme la palabra a mayúsculas, reemplace todas las ‘Ñ’ por ‘N’, y 
# #luego muestre el resultado en pantalla. 

def datos():
    centinela = True 
    contador = 0
    nueva_palabra = ""
    while centinela: 
        palabra = input("Ingrese una palabra:") 
        if "ñ" in palabra and not palabra.isdigit() and not palabra.isspace():
            centinela = False 
            for letra in palabra: 
                contador +=1
                letra = letra.upper()
                if letra == "Ñ":
                    nueva_palabra = nueva_palabra + "N"
                else: 
                    nueva_palabra = nueva_palabra + letra
    print(f"la cantaidad de letras de {palabra} es {contador}")
    print(f" {palabra} se transformo a {nueva_palabra}")
datos()
