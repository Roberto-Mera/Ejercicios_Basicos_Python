"""Escribir un programa que guarde en una variable el diccionario 
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa 
y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario
"""

Divisas={'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
div=str(input("Ingrese una divisa:"))
if div.title() in Divisas:
    print(Divisas[div.title()])
else:
    print("La divisa ingresada no se encuentra en el diccionario.")