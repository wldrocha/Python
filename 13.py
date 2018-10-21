#-*- coding: utf-8 -*-
#ejercicio 13
#Elaborar las siguientes funciones:
#- Una función que reciba un string y nos retorne el primer caracter.
#- Una función que reciba un apellido y un nombre, y nos retorne un único string con el 
# apellido y nombre concatenados y separados por una coma.
#- Una función que reciba dos string y nos retorne el que tiene menos caracteres.

def caracter(string):
    return string[0]
    
def nombreApellido(nombre, apellido):
    return nombre+", "+apellido

def corta(palabra, palabra2):
    if len(palabra)>len(palabra2):
        return "la palabra "+palabra+" Tiene más caracteres"
    if len(palabra2)>len(palabra):
        return "la palabra "+palabra2+" Tiene más caracteres"
    if len(palabra) == len(palabra2):
        return "Tienen los mismos caracteres"

print caracter("hola")
print nombreApellido("wladimir", "Rocha")
print corta("fresa", "manzanilla")