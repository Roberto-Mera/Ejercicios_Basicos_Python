"""Escribir un programa que pida al usuario un número entero positivo 
y muestre por pantalla todos los números impares desde 1 hasta ese número 
separados por comas.
"""
Num=int(input("Ingrese un número:"))

for i in range(Num):
    if (i+1) % 2== 1:
        print(i+1, end=", ")
        i=i+1
    else:
        i=i+1