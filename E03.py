#coding: utf-8
"""
La repartición de ganancias en una empresa se hace en forma proporcional al número de acciones de cada uno de sus tres
socios. Dada la ganancia de un año y la cantidad de acciones de cada sociio, realice un programa en Python que determine
el monto que le corresponde a cada socio
"""

mont_ganan = float(input("Ingrese el monto (S/) de las ganancias:"))
num_socios = 3 # int( input("Ingrese el número de socios:") )
cont=1
acc_socios = []
suma_acc = 0
while(num_socios>0 and cont<=num_socios):
    acciones = float( input("Ingrese las acciones del N° 0" + str(cont) + " :") )
    acc_socios.append( acciones )
    suma_acc = suma_acc + acciones
    cont = cont + 1

monto_socio = []
cont = 1
print("---------------------------------------------------")
for acc in acc_socios:
    monto = ( acc * mont_ganan / suma_acc)
    print("Monto socio N° 0"+str(cont)+" S/ " +str(monto) )
