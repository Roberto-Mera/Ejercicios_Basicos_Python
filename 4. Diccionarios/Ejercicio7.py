"""Escribir un programa que cree un diccionario simulando una cesta de la compra. 
El programa debe preguntar el artículo y su precio y añadir el par al diccionario, 
hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista 
de la compra y el coste total.
"""
cesta={}
continuar="Si"
total=0
while continuar=="Si":
    articulo=input("Ingrese artículo:")
    cesta[articulo]=float(input("Ingrese precio de {}:".format(articulo)))
    total=total+cesta[articulo]
    continuar=str(input("¿Desea introducir un nuevo artículo? (Si/No):"))
cesta["Coste total"]=total

for i in cesta:
    print(i,cesta[i])