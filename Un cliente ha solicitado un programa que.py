# Un cliente ha solicitado un programa que le permita ingresar los mililitros de 
#lluvia caídos diariamente en una semana, para que el programa le informe en 
#pantalla el promedio de precipitación de esa semana.
#  El cliente también desea
#saber cuál fue el día en que más llovió en la semana. 
#A modo ilustrativo, un reporte generado por el programa debería verse como
 #sigue, luego de haber leído las precipitaciones de los 7 días de la semana:
  #El promedio de precipitaciones fue de XX mls. diarios. 
  #El día de más precipitaciones fue el xxxxxx (nombre del día). 
  #Tenga en cuenta que la numeración de los días de la semana comienza con el 1 
  #para el día domingo. 
#Codifique el programa para dar solución a lo solicitado por el cliente. 

suma = 0 
contador = 0
promedio  = 0
auxiliar = 0
dia_max = 0
multiplicacion = 1
for dia in range(1,4):
  # suma= 0
  mililitros = float(input(f"ingrese los mililitros del dia {dia} "))
  suma += mililitros 
  multiplicacion *= mililitros
  contador += 1
  if mililitros >= auxiliar:
    auxiliar = mililitros
    dia_max = dia

  # promedio1 = suma / contador

promedio = suma / contador

print(f"El promedio de precipitaciones fue de {promedio} mls. diarios")
print(f"el dia que mas llovio es: {dia_max}")