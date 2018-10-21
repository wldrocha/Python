#-*- coding:utf-8 -*-
import random
#ejercico #12
#Almacenar en una tupla 5 nombres. Luego generar un valor aleatorio entre 2 y 4. Copiar a una tupla el nombre 
#de la posición indicada por el valor aleatorio y los nombres que se encuentran en la posición anterior y posterior.

nombres = ('alondra', 'adriana','ronald','Jose','ricardo', 'Edras')
aleatorio= random.randint(2,4)
tupla =nombres[aleatorio-1:aleatorio+2]
print tupla