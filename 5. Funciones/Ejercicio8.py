"""Escribir una función que reciba una muestra de números en una lista 
y devuelva un diccionario con su media, varianza y desviación típica.
"""
#Primero crearemos las funciones media, varianza y promedio
def promedio(muestra):
    n=0
    for i in muestra:
        n=n+float(i)
    return n/len(muestra)

def varianza(muestra):
    n=0
    for i in muestra:
        n= n+ pow((float(i) - promedio(muestra)),2)
    return n/(len(muestra)-1)

def desv(muestra):
    return pow(varianza(muestra),0.5)

muestra=input("Ingrese una muestra de números separados por un espacio:").split(" ")
dicc={"Promedio": promedio(muestra),"Varianza":varianza(muestra), "Desviacion típica":desv(muestra)}
print(dicc)
