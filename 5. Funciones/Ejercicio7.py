"""Escribir una función que reciba una muestra de números en una lista y 
devuelva otra lista con sus cuadrados.
"""

def cuadrado(muestra):
    m=[]
    for i in muestra:
        m.append(pow(float(i),2))
    return m

muestra=input("Ingrese una muestra de números separados por un espacio:").split(" ")
print(cuadrado(muestra))