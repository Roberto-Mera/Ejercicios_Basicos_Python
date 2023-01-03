"""Escribir una función que calcule el área de un círculo y otra que calcule 
el volumen de un cilindro usando la primera función.
"""

def Area(r):
    return 3.14*r*r

def Volumen(r,h):
    return Area(r)*h
r=float(input("Ingrese el radio:"))
h=float(input("Ingrese la altura:"))
print("El área del círculo de radio {} es: {}".format(r, Area(r)))
print("El volumen del cilindro de radio {} y de altura {} es: {}".format(r,h,Volumen(r,h)))