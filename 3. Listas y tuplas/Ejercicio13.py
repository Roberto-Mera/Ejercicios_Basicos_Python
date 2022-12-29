"""
Escribir un programa que pregunte por una muestra de números, 
separados por comas, los guarde en una lista y muestre por pantalla 
su media y desviación típica.
"""
lista=list(input("Ingrese los datos:"))

#Podemos remover las "," usando el comando lista.split(",")
while ("," in lista):
    lista.remove(",")

for i in range(len(lista)):
    lista[i]=int(lista[i])
    i=i+1

lista.sort()
"Calculando la media"
N=int(len(lista))
if N%2==0:
    media= (lista[int(N/2)] + lista[int(N/2) -1])/2
else:
    media= lista[int((N-1)/2)]
print(media)
