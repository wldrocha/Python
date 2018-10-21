#-*- coding: utf-8 -*-
import random
#4- Problema Propuesto
#   Generar un valor aleatorio entre -10 y 10. Mostrar un mensaje si el valor generado 
#   es negativo, nulo o positivo. Para generar un valor aleatorio en ese rango debemos 
#   plantear la siguiente expresion: x=-10+random.randint(0,20)
x = -10+random.randint(0,20)
if(x<0):
    print "el numero generado es "+str(x)+" por tanto es negativo"
elif(x>0):
    print "el numero generado es "+str(x)+" por tanto es positivo"
else:
    print "el numero generado es "+str(x)+" por tanto es nulo"
