"""Escribir un programa que pida al usuario un número entero 
y muestre por pantalla un triángulo rectángulo como el de más 
abajo, de altura el número introducido.

*
**
***
****
"""
H=int(input("Ingrese la altura del triángulo:"))
for i in range(H):
    for z in range (i+1):
        print("*",end="")
    print("")
    i=i+1
    