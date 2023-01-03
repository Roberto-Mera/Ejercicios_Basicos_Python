"""Escribir una función que calcule el máximo común divisor de dos números y 
otra que calcule el mínimo común múltiplo.
"""

#Para calcular el mcd de dos números usaremos el algoritmo de Euclides
def mcd(a,b):
    r=a%b
    while(r>0):
        a=b
        b=r
        r=a%b
    return b

#Para calcular el mcm basta con recordar lo siguiente:
# mcd(a.b)*mcm(a,b)=a*b
def mcm(a,b):
    return (a*b)/mcd(a,b)

n1=int(input("Ingrese el primer número:"))
n2=int(input("Ingrese el segundo número:"))
print("El mcd de {} y {} es: {}".format(n1,n2,mcd(n1,n2)))
print("El mcm de {} y {} es: {}".format(n1,n2,mcm(n1,n2)))
