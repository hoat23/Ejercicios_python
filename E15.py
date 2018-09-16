#coding: utf-8
"""
Elabore un programa en Python que permita ingresar un número entero de 3 cifras únicamente y verificar
si el número es correcto, si no es de tres cifras mostrar un mensaje de error. Finalmente, mostrar el número
ingresado al revés.
Ejemplos:

 - Si se ingresa un número de 4 cifras debe mostrar un mensaje de error. "Número incorrecto".
 - Si se ingresa un número de 2 cifras debe mostrar un mensaje de error. "Número incorrecto".
 - Si se ingresa el número 263 debe mostrar el númeor al revés 362.

"""

num = int(input("Ingrese un número entero:"))

if(len(str(num))!=3):
    print("* Número incorrecto *")
else:
    num_str = str(num)
    print("* " + num_str[2] + num_str[1] + num_str[0] + " * ")


