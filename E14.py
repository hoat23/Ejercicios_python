#coding: utf-8
"""
La universidad ofrece una beca de 30% para los estudiantes que cumplan ciertos requisitos. Luego de haber
culminado el primer ciclo de su carrera. Los requisitos son los siguientes:
 - Tener un promedio ponderado mayor o igual a 15.
 - No tener ninguna falta.
Con esta información elabore un algoritmo y representelo mediante un diagrama de flujo que determine el 
otorgamiento de una beca. Los datos que debe ingresar son la nota y la cantidad de faltas.
"""

nota  = float( input("Ingrese la nota   : "))
faltas=   int( input("Ingrese las faltas: "))

if(nota>=15.0 and faltas==0):
    print(" * *   SE OTORGA BECA   * *")
else:
    print(" * * NO SE OTORGA BECA  * * ")