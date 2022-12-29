"""
Escribir un programa que pida al usuario un número entero 
y muestre por pantalla si es un número primo o no.
"""
n=int(input("Ingrese un número:"))
count=0

for i in range(2,n):
    if n%i==0:
        count=count+1
    i=i+1
if(count>0):
    print("{} no es primo".format(n))
else:
    print("{} es primo".format(n))