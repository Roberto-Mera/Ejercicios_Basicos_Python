"""
Escribir un programa que almacene en una lista los números 
del 1 al 10 y los muestre por pantalla en orden inverso 
separados por comas.
"""
Lista=[1,2,3,4,5,6,7,8,9,10]
Lista.sort(reverse=True)
for i in range(len(Lista)):
    print(Lista[i], end=", ")