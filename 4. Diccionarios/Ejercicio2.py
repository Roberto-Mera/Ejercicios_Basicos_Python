"""Escribir un programa que pregunte al usuario su nombre, edad, dirección 
y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla 
el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
"""

#Creamos un diccionario que almacene la información
Inf={"Nombre":"", "Edad":"" , "Dirección":"", "Teléfono":"" }
for i in Inf:
    Inf[i]=input("Ingrese su {}:".format(i))
print("{} tiene {} años, vive en {} y su número es {}".format(Inf["Nombre"], Inf["Edad"],Inf["Dirección"],Inf["Teléfono"]))