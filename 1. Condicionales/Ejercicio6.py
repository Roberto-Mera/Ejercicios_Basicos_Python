"""
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
El grupo A esta formado por las mujeres con un nombre anterior a la M 
y los hombres con un nombre posterior a la N y el grupo B por el resto. 
Escribir un programa que pregunte al usuario su nombre y sexo, y muestre 
por pantalla el grupo que le corresponde.
"""
A_M="abcdefghijklm"
N_Z="nopqrstuvwxyz"
Nombre=str(input("Ingresa tu nombre:"))
Sexo=str(input("Ingresa tu género:"))
Y=Nombre[0].lower()

if (Y in A_M) & (Sexo=="Mujer"):
    print("Perteneces al Grupo A")
if (Y in N_Z) & (Sexo=="Hombre"):
    print("Perteneces al Grupo A")
else:
    print("Perteneces al Grupo B")

