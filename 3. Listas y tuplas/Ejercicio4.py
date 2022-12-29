"""
Escribir un programa que pregunte al usuario los números ganadores 
de la lotería primitiva, los almacene en una lista y los muestre 
por pantalla ordenados de menor a mayor.
"""
Loteria=[]
for i in range(6):
    j=int(input("Ingrese número de la lotería:"))
    Loteria=Loteria+ [j]
    i=i+1

"""Loteria.sort() ordena los elementos de la lista de manera ascendente(creciente),
si quisieramos ordenarlo de manera descendente(decreciente) debemos introducir
el comando Loteria.sort(reverse=True)"""

Loteria.sort()
print(Loteria)