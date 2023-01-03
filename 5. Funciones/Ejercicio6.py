"""Escribir una función que reciba una muestra de números en una lista y devuelva su media."""

def promedio(muestra):
    n=0
    for i in muestra:
        n=n+float(i)
    return n/len(muestra)

muestra=input("Ingrese una muestra de números separados por un espacio:").split(" ")
print(promedio(muestra))