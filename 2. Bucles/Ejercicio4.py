"""Escribir un programa que pida al usuario un número entero positivo 
y muestre por pantalla la cuenta atrás desde ese número hasta cero separados 
por comas.
"""
Num=int(input("Ingrese un número:"))
for i in range(Num):
    print(Num-i, end=", ")
print(0)