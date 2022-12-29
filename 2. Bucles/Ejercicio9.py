"""
Escribir un programa que almacene la cadena de caracteres contraseña 
en una variable, pregunte al usuario por la contraseña hasta que introduzca 
la contraseña correcta.
"""
Pass=str(input("Ingrese la contraseña:"))
Contraseña="Peluche1234"
while Pass!=Contraseña:
    print("Contraseña incorrecta")
    Pass=str(input("Ingrese de nuevo la contraseña:"))

print("Contraseña correcta")