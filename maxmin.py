# muestre el minimo y el maximo de 5 numeros ingresado por el usuario


for orden in range(1,6):
    ingreso = int(input(f"ingrese el numero de orden {orden} "))
    
    if orden == 1:
        maximo = ingreso
        minimo = ingreso
        pos_min = orden
        pos_max = orden

    if ingreso > maximo:
        maximo = ingreso 
        pos_max = orden

    if ingreso < minimo:
        minimo = ingreso
        pos_min = orden
        
# print(float('inf') >  99999999999)
print(f"el maximo es {maximo} y el orden es {pos_max} y el minimo es {minimo}  y el ordenb es {pos_min}")       