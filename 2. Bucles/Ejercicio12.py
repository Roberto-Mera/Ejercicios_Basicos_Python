"""Escribir un programa en el que se pregunte al usuario 
por una frase y una letra, y muestre por pantalla el número 
de veces que aparece la letra en la frase.
"""
Frase=str(input("Ingrese una frase:"))
Letra=str(input("Ingrese una letra:"))
Count=0
Frase=Frase.lower()
Letra=Letra.lower()
for i in range(len(Frase)):
    if Frase[i]==Letra:
        Count=Count+1
    i=i+1
print("La letra {} aparece {} veces".format(Letra,Count))

