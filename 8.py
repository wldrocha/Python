#-*- coding: utf-8 -*
#ejercicio #8
#   Desarrollar una funcion que reciba dos enteros y nos muestre todos 
#   los valores comprendidos entre ellos (el segundo parametro siempre debe ser mayor al primero)
def digitos():
    a= input("introduzca el primer digito: ")
    b= input("introduzca el segundo digito: ")
    if a>b:
        print "el primer parámetro debe ser menor "
        digitos()
    n=a
    while n<=b:
        print n
        n = n+1
digitos()