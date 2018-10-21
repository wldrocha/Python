#-*- coding: utf-8 -*-
#ejercicio #14
#Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a

nombres = ['alondra', 'adriana','ronald','Jose','ricardo', 'Edras']
i = 0
contador =0

while i<len(nombres):
    if nombres[i][0] == "a":
       contador = contador+1
    i=i+1
print "La cantidad de nombres que empiezan con la letra a son: "+str(contador)