lista = ["Eduardo",23,True]
"La tupla no se puede modificar y sus datos se añaden dentro de parentesis en lugar de corchetes"
tupla = ("Eduardo",23,True)
#Se puede
lista[1] = 10
#No se puede
#tupla[1] = 10

'''Creando un conjunto set, para crearlo usamos llaves
El conjunto set se puede redefinir pero no se pueden modificar sus elementos
No se accede a elementos por indices
no permite repetir valores
son desordenados
'''
conjunto ={"Eduardo",23,True}
 

#Creando un diccionario
diccionario = {
    "nombre": "Eduardo",
    "Edad": 23,
    "Vivo":True
}


#Operadores
#Potencia-> **
exponente = 5**2

#division baja //
#Devuelve un entero redondeado hacia abajo
division = 12//5

tipo_dato = type(division)
print(tipo_dato)

