#coding: utf-8
"""
Una ooperadora de telefonía necesita calcular el recibo de consumo, el cual se obtiene de la siguiente manera:
 - Si consume 4GB o menos paga S/50 por mes
 - Si consume más de 4GB, hasta de 8GB paga paga S/85 por mes y por cada GB de consumo adicional pagará S/ 4.50
"""

datos = float(input("Ingrese los datos consumidos [Giga Bytes]: "))

if( datos <= 4):
    pago = 50.0
else:
    if( datos <= 8):
        pago = 85.0
    else:
        pago = 85.0 + (datos - 8) * 4.50

print("El monto a pagar es S/ "+ str(pago) )
