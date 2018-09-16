#coding: utf-8
"""
Una empresa de ventas de piezas de automóviles necesita un programa en Python que le permita determinar el precio al
que debe vender una pieza considerando un porcentaje de ganancia. Para ello se leerán el precio de compra de la pieza
y el procentaje de ganancia que se desea obtener la empresa en tanto por ciento.
"""

porc_gan = float(input("Ingrese el porcentaje de ganancia : "))
cost_pz  = float(input("Ingrese el costo (S/) de la pieza : "))

porc_cst = (100-porc_gan)
# porc costo     -> costo pieza soles
# porc venta:100 -> precio venta soles
# precio venta = porc_venta * cost_pieza /porc_costo
vent_pz  =  (100 * cost_pz / porc_cst)
print("Precio de venta de la pieza es S/"+str(vent_pz))