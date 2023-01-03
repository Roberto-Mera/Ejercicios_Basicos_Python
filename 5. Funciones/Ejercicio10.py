"""Escribir una función que convierta un número decimal en binario y 
otra que convierta un número binario en decimal.
"""
def binario(n):
    q=n//2
    r1=n%2
    r=[str(r1)]
    while(q>0):
        n=q
        q=q//2
        r.append(str(n%2))
    r.reverse()
    return ''.join(r)

def decimal(n):
    n=str(n)
    m=0
    for i in range(len(n)):
        m=m+int(n[i])*pow(2,len(n)-i-1)
    return m

n1=int(input("Ingrese el número que desee convertir a binario:"))
n2=int(input("Ingrese el binario que desee convertir a decimal:"))
print("{} en binario es: {}".format(n1,binario(n1)))
print("{} en decimal es: {}".format(n2,decimal(n2)))