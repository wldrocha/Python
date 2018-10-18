import random
#ejercicio #5
#	Generar 3 numeros aleatorios entre 1 y 100. Mostrar un mensaje si todos son 
#	superiores a 10.
x1= random.randint(0,100)
x2= random.randint(0,100)
x3= random.randint(0,100)
print "los numeros generados son "
print x1
print x2
print x3
if(x1>10 and x2>10 and x3>10):
    print "todos los numeros son mayores a 10"
elif(x1>10 and x2>10 or x1>10 and x3>10 or x2>10 and x3>10):
    print "Solo dos numeros son mayores a 10"
else:
    print "ninguno de los numeros son mayores a 10"

