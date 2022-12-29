"""
Escribir un programa que almacene el abecedario en una lista, 
elimine de la lista las letras que ocupen posiciones múltiplos de 3, 
y muestre por pantalla la lista resultante.
"""
abecedario="a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z"
lista=abecedario.split(",")
multiplos=[]
for i in range(len(lista)):
    if (i+1)%3==0:
        multiplos.append(lista[i])
print(multiplos)
