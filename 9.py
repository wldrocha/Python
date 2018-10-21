# -*- coding: utf-8 -*-
#ejercicio #9
#Desarrollar una función que reciba tres enteros y nos retorne la suma de los dos más grandes.
def suma(a,b,c):
    if a>b and a>c:
        if b>c:
            return a+b
        else:
            return a+c
    elif b>a and b>c and c>a:
        return b+c
    else:
        return c+a
print suma(5,9,7)
    #x = 5 input('Introduzca el primer dígito')
    #y = 4 input('Introduzca el segundo dígito')
    #z = 3 input('instroduzca el tercer dígito')