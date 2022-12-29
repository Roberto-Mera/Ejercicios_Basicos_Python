"""Escribir un programa que pregunte al usuario su renta anual y muestre 
por pantalla el tipo impositivo que le corresponde.
"""
ra=float(input("Ingrese su renta anual:"))
if ra<10000:
    ti=0.05
if ra>=10000 and ra<20000:
    ti=0.15
if ra>=20000 and ra<35000:
    ti=0.20
if ra>=35000 and ra<60000:
    ti=0.30
if ra>=60000:
    ti=0.45
print("Tipo impositivo correspondiente:",ra*ti)