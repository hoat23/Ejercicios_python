#coding: utf-8
"""
SEDALIB requiere determinar el pago que debe realizar una persona por el total
de metros cubicos que consume de agua al llenar una piscina.
"""

prec_m3 = float( input("Ingrese el costo (S/) por metro cúbico de agua:"))

print("Ingrese las dimensiones de la piscina:")
l = float( input("Largo [metros]:") )
w = float( input("Ancho [metros]:") )
h = float( input("Alto  [metros]:") )

vol = l * w * h

print("Las dimensiones de la piscina son LxWxH: "+str(l)+"x"+str(w)+"x"+str(h)+"[m3]")
print("Volumen de agua "+ str(vol) + "[m3]")
print("Monto a pagar S/"+ str(prec_m3*vol)+"\n")
