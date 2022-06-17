# Escriba una función en Python que permita procesar el título y la cantidad de      
# visualizaciones de 150 videos de YouTube.                                      
# Por ejemplo, una entrada válida del programa sería “Manejo de Listas”            
# para el título y 2500 para las visualizaciones.                                 
# Una vez procesados todos los videos, el programa debe informar:                  
#   El promedio de visualizaciones de los videos.                                    
#   Indicar (por sí o por no) si algún vídeo posee como título “Boca Campeón 2022”.        
#   El título del video con mayor cantidad de visualizaciones.                    

def procesar_videos():
    suma = 0
    boca_campeon = 'No'
    titulo_mayor = ''
    for i in range(3):
        titulo = input('Ingrese el titulo del video: ')
        visualizaciones = int(input('Ingrese la cantidad de visualizaciones: '))
        
        if i == 0:
             mayor_visualizaciones = visualizaciones
             titulo_mayor = titulo
        
        suma += visualizaciones
        if titulo == "Boca Campeón 2022":
            boca_campeon = 'Si'
        if visualizaciones > mayor_visualizaciones:
            mayor_visualizaciones = visualizaciones
            titulo_mayor = titulo
        
    promedio = suma / 150
    print(f"El promedio de visualizaciones es: {promedio}")
    print(f"Boca campeon?: {boca_campeon}")
    print(f"El video con mayor cantidad de visualizaciones es: {titulo_mayor}")
    
#procesar_videos()                                                         texto        resultado   i
#                                                                     39‘Programación’          
#                                                                      40                 False
# Consigna 3:                                                          41                          P
# Escriba una función que reciba un string como parámetro y retorne                          
# un booleano que identifique si existe la letra ‘a’ en el mismo.      41                          r
# Por ejemplo, si la función recibe ‘Programación’ retornará True.     41                          o
#                                                                      41                          g 
def esta_a(texto): #                                                   41                           r
    resultado = False #                                                41                           a
    for i in texto:                                              #     43               True
        if i == 'a':                                             #     41                           m       
            resultado = True                                     #     41                           a  
    return resultado  #                                                43              True 
                                                            #          41                           c
def esta_a_2(texto):
    return 'a' in texto

#print(esta_a('Programación'))


# Consigna 4:
# Escriba una función en Python que reciba como parámetro una lista y 
# retorne la cantidad de elementos positivos y negativos. 
# Así, si por ejemplo la función recibe la lista 
# L = [5, 9, -10, 11, 3, 8, 21, -2] deberá retornar 6 y 2 respectivamente .
lista = []
lista = list()

def consignas(lista):
    cantidad_positivos = 0
    cantidad_negativos = 0
    for i in range (len(lista)):
        if lista[i] > 0:
            cantidad_positivos += 1
        else:
            if lista[i] < 0:
                cantidad_negativos += 1
    return cantidad_positivos, cantidad_negativos
    
def consignas2(lista):
    cantidad_positivos = 0
    cantidad_negativos = 0
    for i in lista:
        if i % 2 == 0:
            cantidad_positivos += 1
        else:
            cantidad_negativos += 1
    return cantidad_positivos, cantidad_negativos

print(consignas2([5, 9, -10, 11, 0, 8, 21, -2]))