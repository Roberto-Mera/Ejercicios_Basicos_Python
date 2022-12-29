"""
Escribir un programa que pida al usuario una palabra y 
muestre por pantalla el número de veces que contiene cada vocal.
"""
Pal=str(input("Ingrese una palabra:"))
Vocales=["a","e","i","o","u"]
P=list(Pal)
count=0
for i in range(len(Vocales)):
    for j in range(len(P)):
        if Vocales[i]==P[j]:
            count=count+1
            j=j+1
    print("La vocal {} aparece {} veces".format(Vocales[i],count))
    count=0
    i=i+1