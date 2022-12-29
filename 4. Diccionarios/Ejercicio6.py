"""Escribir un programa que cree un diccionario vacío y lo vaya llenado 
con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, 
correo electrónico, etc.) que se le pida al usuario. 
Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""
Info={}
Continuar="Si"
while Continuar=="Si":
    clave=input("Ingrese un campo:")
    Info[clave]=input("Ingrese la información del campo {}:".format(clave))
    print(Info)
    Continuar=str(input("Desea continuar (Si/No):" ))