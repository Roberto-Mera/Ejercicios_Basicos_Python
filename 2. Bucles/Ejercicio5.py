"""Escribir un programa que pregunte al usuario una cantidad a invertir, 
el interés anual y el número de años, y muestre por pantalla el capital 
obtenido en la inversión cada año que dura la inversión."""
Cap=float(input("Ingrese el capital:"))
Interes=float(input("Ingrese la tasa de interés anual:"))
Año=int(input("Ingrese los años a invertir:"))
Porcentaje=Interes/100

for i in range(Año):
    Cap = Cap + Porcentaje*Cap
    i=i+1
    print("Su capital tras {} años será de {} soles".format(i,Cap))
