#ejercico9
#Definir una tupla que almacene 5 enteros. Implementar un algoritmo que imprima la 
#suma de todos los elementos

tupla=(1,2,3,4,5)
indice = 0
suma = 0
while indice<len(tupla):
    suma = tupla[indice]+suma
    indice = indice+1
    
print suma
