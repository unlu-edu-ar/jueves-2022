# 10. Escribir una función que reciba una cadena de unos 
# y ceros (es decir, un número en representación binaria) 
# y devuelva el valor decimal correspondiente.

def binario_a_decimal(binario):
    suma=0
    ultimo_indice = len(binario) -1
    for i in range(0,len(binario)):
        nuevo_indice = ultimo_indice - i
        
        suma+= int(binario[nuevo_indice])*(2**i)
    return suma

print(binario_a_decimal("1010101"))