#coding: utf-8
"""
Se requiere determinar el tiempo que tarda una persona en llegar de una ciudad a otra en bicicleta, considerando que lleva
una velocidad constantes. Construya un programa python.
"""

distancia = float( input("Ingrese la distancia a recorrer [metros]         :") )
velocidad = float( input("Ingrese la velocidad de la bici [metros/segundos]:"))

tiempo = distancia / velocidad
print("El tiempo que demora una persona en recorrer el ciclista es "+str(tiempo)+"[segundos]")