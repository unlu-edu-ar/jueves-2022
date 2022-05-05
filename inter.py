# Cree una función que recibe dos números enteros positivos n1 y n2 como 
# parámetros, donde n1 < n2, y retorna el resultado de sumar los números enteros 
# contenidos en el intervalo [n1...n2]


def testSumatoria():
    print('Testeando testSumatoria()... ', end='')
    assert sumatoria(1, 3) == 6 
    assert sumatoria(5, 6) == 11
    assert sumatoria(3, 7) == 25
    print('Pasó!')

def sumatoria(n1, n2):
    # n1 = 1 
    # n2 = 3
    resultado = 0
    for i in range (n1,n2+1):
        resultado = resultado + i
    return resultado

testSumatoria()