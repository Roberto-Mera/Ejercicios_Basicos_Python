"""
Escribir un programa que guarde en un diccionario los precios de las frutas 
de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre 
por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el 
diccionario debe mostrar un mensaje informando de ello.
"""
Lista={"Plátano":1.35, "Manzana":0.80, "Pera":0.85, "Naranja":0.70}
Fruta=str(input("Ingrese una fruta:")).title()
Kilos=float(input("Cuantos kilos de {} compraste:".format(Fruta)))
if Fruta in Lista:
    print("Por {} kilos de {} pagaste:{} soles".format(Kilos,Fruta,Lista[Fruta]*Kilos))
else:
    print("{} no se encuentra en la lista".format(Fruta))