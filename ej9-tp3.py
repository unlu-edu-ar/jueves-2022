# Cree un script que, sabiendo cuántos pesos argentinos tiene una persona
# ahorrada en su cuenta (almacenando ese monto en una variable), muestre
# en pantalla los montos convertidos en dólares (U$1 = $80.5), reales ($R1 =
# $14.1), y euros (€1 = $69.5). La salida del programa debe tener el siguiente
# formato:

ahorro = 1000
dolares = ahorro / 102.5
reales = ahorro / 14.1
euros = ahorro / 104.5

print ("Ahorro en Pesos: ", round(ahorro, 1))
print ("Ahorro en Dolares: ", round(dolares, 1))
print ("Ahorro en Reales: ", reales)
print ("Ahorro en Euros: ", euros)