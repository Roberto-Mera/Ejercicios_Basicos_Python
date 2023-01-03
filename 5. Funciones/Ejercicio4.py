"""Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y 
devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, 
deberá aplicar un 21%.
"""

def fact(n1,n2):
    if n2=="":
        n2=21
    else:
        n2=float(n2)
    return n1*(n2/100)
cantidad_sin_IVA=float(input("Ingrese cantidad:"))
IVA=str(input("Ingrese porcentaje de IVA:"))
print(fact(cantidad_sin_IVA,IVA))
