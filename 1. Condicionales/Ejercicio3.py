"""
Escribir un programa que pida al usuario dos números y
 muestre por pantalla su división. 
 Si el divisor es cero el programa debe mostrar un error.
"""
Dividendo=int(input("Ingrese el dividendo:"))
Divisor=int(input("Ingrese el divisor:"))

if Divisor==0:
    print("El divisor no puede ser cero:")
    Divisor=int(input("Ingrese un nuevo valor distinto de cero:"))
print(Dividendo/Divisor)
