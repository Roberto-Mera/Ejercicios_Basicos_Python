"""
Escribir un programa que pida al usuario una palabra 
y luego muestre por pantalla una a una las letras de 
la palabra introducida empezando por la última.
"""
Word=str(input("Ingrese una palabra:"))
n=len(Word)
print(Word[1])
for i in range(n-1,-1,-1):
    print(Word[i],end="")
