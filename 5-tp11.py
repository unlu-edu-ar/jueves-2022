# Modificar el ejercicio anterior para que en lugar de devolver una nueva lista,
# modifique la lista dada para invertirla. Usar listas auxiliares.

def invertir_lista(lista):
    lista_auxiliar = []
    ultimo_indice = len(lista) - 1
    for i in range(len(lista)):
        nuevo_indice = ultimo_indice - i
        lista_auxiliar.append(lista[nuevo_indice])
    
    return lista_auxiliar

lista = ['Di', 'buen', 'día', 'a', 'papa']
# lista = invertir_lista(lista)

# print(lista)

def invertida ():
    l=['Di', 'buen', 'día', 'a', 'papa']
    ling=[]
    for i in range(1, len(l)+1):
        ling.append(l[i*(-1)])
    l=ling
    return l
#print(invertida())



def invertida(l):
    nueva_lista = []
    for i in l[::-1]:
        nueva_lista.append(i)
    return nueva_lista

print(invertida(lista))

def es_primo(numero):
    cantidad = 0
    for i in range(1,numero+1):
        if numero % i == 0:
            cantidad += 1

    return cantidad == 2
print(es_primo(10))
