# Cree una función que recibe un string s de longitud > 0, y dos números enteros 
# naturales n y m, donde 0<=n<=m<len(s), y retorna un nuevo string t que 
# es el string s sin la subcadena s[n1..n2]. 

def borrarSubcadena(s,n,m):
    a = s[:n]
    print(a)
    b = s[m+1:]
    print(b)
    return a+b 

def borrarSubcadena2(s,n,m):
    respuesta=""
    for indice in range(len(s)):
        if indice < n or indice > m:
            respuesta = respuesta + s[indice]
    return respuesta

print("ej1",borrarSubcadena("agustincapo",3,6))
print("ej2",borrarSubcadena2("agustincapo",3,6))