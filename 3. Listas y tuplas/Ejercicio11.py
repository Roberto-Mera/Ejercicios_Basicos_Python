"""
Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) 
en dos listas y muestre por pantalla su producto escalar.
"""
v1=list((1,2,3))
v2=list((-1,0,2))
ps=0
for i in range(3):
    ps=ps+ v1[i]*v2[i]
    i=i+1
print("El producto escalar es:",ps)
