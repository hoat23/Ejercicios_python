#coding: utf-8
"""
Elabore un programa en Python que calcule e imprima el sueldo básico, el sueldo bruto y el sueld neto de 
un trabajador. Si se sabe que el cálculo del pago mensual de un empleado de una empresa se efectúa de la siguiente
manera:
 - Sueldo básico se calcula en base al número total de horas trabajadas basado en una tarifa horaria
 - Al sueldo básico, se le aplica una bonificación del 18% del mismo obteniéndose el sueldo bruto.
 - Al sueldo bruto, ses le aplica un descuento del 12% obteniéndose el sueldo neto.
"""

pag_hr =  float( input("Ingrese el pago (S/) por cada hora   : "))
num_hrs = float( input("Ingrese el número de horas trabajadas: ") )

sld_basico = num_hrs * pag_hr
sld_bruto  = 1.18 * sld_basico
sld_neto   = (1-0.12) * sld_bruto

print("---------------------------------------------------------")
print("Sueldo basico S/" + str(sld_basico))
print("Sueldo bruto  S/" + str(sld_bruto))
print("Sueldo neto   S/" + str(sld_neto))

