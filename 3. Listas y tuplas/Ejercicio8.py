"""Escribir un programa que pida al usuario una palabra y 
muestre por pantalla si es un palíndromo.
"""
Palabra=str(input("Ingrese una palabra:"))
Original=list(Palabra)
Reversa=list(Palabra)
Reversa.reverse()

if Original==Reversa:
    print("La palabra ingresada es un palíndromo")
else:
    print("La palabra ingresada no es un palíndromo")
