"""Escribir una función a la que se le pase una cadena <nombre> y muestre 
por pantalla el saludo ¡hola <nombre>!.
"""

def Saludo(nombre):
    print("Hola", nombre+ "!")
    return

nombre=str(input("Ingrese su nombre:"))
Saludo(nombre)