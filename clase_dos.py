# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 19:14:00 2021

@author: amand
"""
# Condicionales

# Tabla de verdad

# Tabla del and
# v and v = v

print(True and True)
print(True and False)
print(False and True)
print(False and False)

# Tabla del or

print(True or True)
print(True or False)
print(False or True)
print(False or False)

# Negacion

print(not True)
print(not False)

# Mas de dos condiciones al mismo tiempo

print(True and False or False or True or True)
print(True and True) or False or (True or True)

# Estructura if
x = -1
if(x > 0):
    print('1')
else:
    print('2')
print('3')

# HUA que dada la edad de una persona indique si es mayor
# o menor de edad

edad = int(input('Digite su edad: '))
if(edad >= 18):
    print('Usted es mayor de edad')
else:
    print('Usted es menor de edad')

# HUA que indique si un estudiante aprobo o reprobo una
# asignatura teniendo en cuenta que aprueba con minimo
# una calificacion de 3.0 hasta 5.0

nota_final = float(input('Digite la nota final: '))
if(nota_final > 3.0 and nota_final < 5.0):
    print('Usted aprobo la asignatura')
elif(nota_final < 3.0 and nota_final > 0):
    print('Usted reprobo la asignatura')
else:
    print('La nota ingresada no es valida')

# HUA que dado un numero n diga si es negativo, positivo o cero.

n = float(input('Digite un numero: '))
if (n < 0):
    print('El numero {n} es positivo')
elif (n < 0):
    print('El numero {n} es negativo')
else:
    print('El numero es cero')
    