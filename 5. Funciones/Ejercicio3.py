"""Escribir una función que reciba un número entero positivo y devuelva su factorial."""

def fact(n):
    m=1
    for i in range(n):
        m=m*(i+1)
        i=i+1
    return m

n=int(input("Ingrese un número:"))
print(fact(n))