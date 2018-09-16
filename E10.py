#coding: utf-8
"""
Elabore un porgrama en Python que permita mostrar el estado del alumno, según la nota final del curso . Para ello 
debe tener en cuenta los siguientes criterios:
 - Si la nota es menor de 10.50 está desaprobado.
 - Si la nota es mayor de 10.50 y menor de 20 está aprobado.
"""

num_alum = int(input("Ingrese el número de alumnos : "))

for n in range(0,num_alum):
    nota = float(input("Ingrese la nota del alumno N°0"+str(n+1)+" : "))
    if(nota>20 and nota <0):
        print("ERROR: La nota no es valida.")
    
    if(nota<10.50):
        print("\t * DESPROBADO *")
    else:
        if(nota<20.0):
            print("\t * APROBADO *")
