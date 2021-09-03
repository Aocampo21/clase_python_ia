# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 04:19:55 2021

@author: amand
"""

print('Hello world')

# Variables
a = 5
print(type(a))
a = "Hola"
print(type(a))
a = 3.5
print(type(a))
a = True
print(type(a))

# Suma
a = 5
b = 2
c = a + b
print(c)

# Resta
a = 5
b = 2
c = a - b
print(c)

# Multiplicacion
a = 5
b = 2
c = a * b
print(c)

# Division
a = 5
b = 2
c = a / b
print(c)

a = 5
b = 2
c = a // b
print(c)

# Potencia
a = 5
b = 2
c = a ** b
print(c)

# Raiz
a = 5
c = a ** (1/2)
print(c)

# import math
# raiz = math.sqrt(25)
# print(raiz)

# Conversiones

a = 3
y = str(a)
print(y)
print(type(y))

# Concatenaciones

a = "hola"
b = "mundo"
c = a + b

a = 'Hola'
b = a * 5

# Imprimir por pantalla

nombre = input('Digite su nombre')
print('Hola', nombre)

# Haga un algoritmo que sume dos numeros e imprima su resultado

n1 = float(input('Digite el numero uno: '))
n2 = float(input('Digite el numero dos: '))
suma = n1 + n2
# print(suma)
# print('La suma es: ', suma)
print(f'La suma de los numeros {n1} + {n2} es {suma}')

# HUA que lea un numero y lo eleve al cuadrado

a = int(input('Digite un numero'))
b = a ** 2
print(f'La potencia del numero {a} es {b}')

# HUA que tome el valor de un producto le aplique el 20% de descuento,
# imprima el valor del producto inicial, el valor con descuento y el valor
# ahorrado

a = float(input('Digite el valor del producto: $'))
descuento = a * 0.20
Vfinal = a - descuento
print(f'El valor incial del producto es: ${a:,}')
print(f'El valor incial del descuento es: ${descuento:,}')
print(f'El valor incial del ahorrado es: ${Vfinal:,}')
