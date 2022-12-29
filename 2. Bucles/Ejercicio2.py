"""Escribir un programa que pregunte al usuario su edad y muestre 
por pantalla todos los años que ha cumplido (desde 1 hasta su edad)
"""
Edad=int(input("Ingrese su edad:"))
for i in range(Edad):
    print("Has cumplido {} años".format(i+1) )