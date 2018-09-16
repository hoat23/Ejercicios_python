#coding: utf-8
"""
Construya un programa en Python que calcule el sueldo bruto, el descuento por ESSALUD, el descuento por AFP
y el sueldo neto del empleado de una empresa de acuerdo a los siguientes criterios:
 - El sueldo bruto se calcula multiplicando el número de horas trabajadas por una tarifa horaria.
 - El descuento por ESSALUD es igual al 9% del seuldo bruto.
 - El descuento por AFP es igual al 11.5% del sueldo bruto.
 - El sueldo neto es la diferencia entre el sueldo bruto y el descuento total.
"""


pag_hr =  float( input("Ingrese el pago (S/) por cada hora   : "))
num_hrs = float( input("Ingrese el número de horas trabajadas: ") )

sld_bruto   = pag_hr * num_hrs
des_essalud = 0.09 * sld_bruto
des_afp     = 0.115* sld_bruto

des_total   = des_essalud + des_afp
sld_neto    = sld_bruto - des_total

print("--------------------------------------------------")
print("Sueldo bruto      +S/ "+ str(sld_bruto))
print("Descuento ESSALUD -S/ "+ str(des_essalud))
print("Descuento AFP     -S/ "+ str(des_afp))
print("---------------------------------------------------")
print("Salario neto      S/ "+ str(sld_neto))


