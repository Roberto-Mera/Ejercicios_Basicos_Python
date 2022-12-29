"""Escribir un programa que almacene las matrices en una lista y muestre por pantalla su producto.
"""
A=[[1,2,3],[4,5,6]]
B=[[-1,0],[0,1],[1,1]]
C=[[0,0],[0,0]]
for i in range(2):
    for j in range(2):
        for k in range(3):
            C[i][j]=C[i][j]+A[i][k]*B[k][j]
            k=k+1
        j=j+1
    i=i+1
print(C)