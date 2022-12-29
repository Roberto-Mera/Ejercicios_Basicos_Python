#Agregar .lower() a un texto vuelve el texto a minúscula
"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
por el usuario coincide con la guardada en la variable 
sin tener en cuenta mayúsculas y minúsculas.
"""
contraseña="peluche1234"
x=str(input("Ingresa la contraseña:"))
if contraseña==x.lower(): 
    print("La contraseña es correcta.")
else:
    print("La contraseña es incorrecta.")