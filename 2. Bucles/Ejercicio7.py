"""
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
"""

print("*******************************")
for i in range(1,11):
    for j in range(1,11):
        print("{}x{}={}".format(i,j,i*j),end="\t")
        j=j+1
    print("")
    i=1+1

print("*******************************")