#coding: utf-8
"""
Elabore un programa en Python que permita calcular el peso ideal de una persona según el sexo
y la altura expresado en cm, considere los siguientes valores según sea el caso:
 - Varon(V) = 0.75 * tall_varon - 62.5
 - Mujer(M) = 0.60 * tall_mujer - 40.0
"""

sexo = int(input("Ingrese el sexo (1->varon & 2->mujer): "))
talla= float(input("Ingrese la talla [cm]: "))

if(sexo==1):
    peso = 0.75 * talla - 62.5
else:
    if(sexo==2):
        peso = 0.60 * talla - 40.0
    else:
        print("ERROR: sexo debe tener un valor valido 1 o 2.")
        exit()

print("El peso ideal es " + str(peso))
    
