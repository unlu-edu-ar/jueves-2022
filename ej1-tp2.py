# Cree un script que almacene un número entero en una variable, y luego
# muestre en pantalla su valor absoluto, con el mensaje “El valor absoluto de N
# es |N|”. Finalmente, verifique que su programa funciona correctamente,
# ejecutándolo con el valor 10 en la variable (la salida debería ser 10), y luego
# con el valor -10 (la salida debería ser 10 nuevamente).

numero1 = -10

valor_absoluto = abs(numero1)

print("El valor absoluto de", numero1, "es", valor_absoluto)
print("El valor absoluto de " + str(numero1) + " es " + str(valor_absoluto))
resultado = f"El valor absoluto de {numero1} es {valor_absoluto}"
print(resultado)