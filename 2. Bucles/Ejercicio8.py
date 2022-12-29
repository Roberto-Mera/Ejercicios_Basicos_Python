"""
Escribir un programa que pida al usuario un número entero y 
muestre por pantalla un triángulo rectángulo como el de más abajo.

1
3 1
5 3 1

"""
H=int(input("Ingrese la altura del triángulo:"))
for i in range (H):
    for j in range(2*i + 1,0,-2):
        print(j, end=" ")
        j=j+1
    print("")
    i=i+1