#-*- coding: utf-8-*-
#ejercicio #15
#Definir una lista con una serie de elementos. Intercambiar la información del primero con el último de la lista.
lista =[6,2,3,4,5,1]
print "lista desordenada: "+str(lista)
n1 = lista[0]
n2 = lista[-1]
del(lista[0])
del(lista[-1])
lista[0:0]=[n2]
lista[-1:-1]=[n1]
print "lista ordenada: "+str(lista)