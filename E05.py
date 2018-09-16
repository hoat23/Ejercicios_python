#coding: utf-8
"""
Una tienda ha puesto en oferta la venta de un producto ofreciendo un determinado porcentaje de descuento
sobre el importe de la compra. Elabore un programa Python que determine el importe de la compra, el importe
del descuento y el importe a pagar por la compra de cierta cantidad de unidades del producto
"""

descuento = float(input("Ingrese el porcentaje de descuento: "))
num_prod =   int(input("Ingrese el numero de productos    : "))
imp_prod = [] #Almacena el precio de costo de cada producto
des_prod = [] #Almacena el importe del descuento
pag_prod = [] #Almacena el importe a pagar por el producto despues de descontar
if(descuento>100):
    print("Error: El descuento no puede ser mayor que el 100%")
    exit()

for n in range(1,num_prod+1):
    precio_prod = float( input("Costo del producto N°0"+str(n)+" : ") )
    imp_prod.append( precio_prod )
    des_prod.append( precio_prod * descuento/100.00)
    pag_prod.append( precio_prod * (1-descuento/100.00))
    n = n + 1

for n in range(0,num_prod):
    print("Producto N°0"+str(n+1)+": ")
    print("\tCosto        : S/"+str(imp_prod[n]))
    print("\tDescuento    : S/"+str(des_prod[n]))
    print("\tMonto a pagar: S/"+str(pag_prod[n]))
