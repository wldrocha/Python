import random
#ejercicio #6
#	Generar un valor aleatorio comprendido entre 1 y 5.
#	Luego mostrar en castellano el valor generado
x = random.randint(1,5)
if(x==1):
    print "El valor generado es uno"
elif(x==2):
    print "El valor generado es dos"
elif(x==3):
    print "El valor generado es tres"
elif(x==4):
    print "El valor generado es cuatro"
else:
    print "el valor generado es cinco"