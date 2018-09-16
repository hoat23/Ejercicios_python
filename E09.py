#coding: utf-8
"""
Una empresa desea determinar el monto de un cheque que debe proporcionar a uno de sus empleados que tendrá que ir por un 
número determinado de días a la ciudad de Trujillo. Los gastos que cubre la empresa son: hotel, comida y 100 dolares
diarios para otros gastos. El monto debe estar desglosado para cada uno de los tres conceptos. Elabore un programa
en Python que permita determinar el monto del cheque
"""

hotel = float(input ("Ingrese el precio(S/) diario del hotel : "))
comida= float(input("Ingrese los gastos(S/) de comida        : "))
dias  = float(input("Ingrese el número de días               : "))

gastos_hotel = hotel * dias
otros_gastos = dias * 100
gastos_totales = gastos_hotel + comida + otros_gastos

print("--------------------------------")
print(" Detalle de gastos :")
print("--------------------------------")
print("Comida S/ "+str(comida))
print("Hotel  S/ "+str(gastos_hotel))
print("Otros  S/ "+str(otros_gastos))
print("--------------------------------")
print("TOTAL  S/ "+str(gastos_totales))