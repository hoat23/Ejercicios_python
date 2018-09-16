#coding: utf-8
"""
Tres socios, Alberto, Lilina, Erika aportan cantidades de dinero para formar un capital.
Elabore un programa en python que permita determinar el capital total formado y el porcentaje de dicho capital
que aporta cada uno.
"""

alberto = float(input("Ingrese monto(S/) de Alberto :" )) 
lilina  = float(input("Ingrese monto(S/) de Lilina  :" ))
erika   = float(input("Ingrese monto(S/) de Erika   :" ))

total = alberto + lilina + erika

print("\nCapital total S/" + str(total) )
print("Alberto " + str( alberto/total) +"  %")
print("Lilina  " + str( lilina/total)  +"  %")
print("Erika   " + str( erika/total)   +"  %")
