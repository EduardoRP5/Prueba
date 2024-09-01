'''Metodos con cadenas:
DIR -> Devuelve la lista de atributos validos del objeo pasado

UPPER -> Convierte a mayusculas
LOWER -> Convierte a minuscula
CAPITALIZE -> primera letra en mayuscula 

FIND -> Encuentra la primera aparicion del valor especificado, sino devuelve -1
INDEX -> encuentra la primera aparicion del valor especificado, sino devuelve una excepcion 
 
ISUMERIC -> si es numerico devuelve true
ISALPHA -> si es alfa numerico devuelve true
 
COUNT -> devuelve el numero de ocurrencias de una subcadena en la cadena dada
LEN -> CUENTA LOS CARACTERES DE UNA CADENA

ENDSWITH -> verifica si una cadena  con
STARTSWITH -> verifica si una cadena con

REPLACE -> remplaza un valor por otro
SPLIT -> separa por el parametro dado'''

cad1 = "ya me aburri"
cad2 = "Zzzzzzzzzz"

#Mayusculas y minusculas
mayuscula = cad1.upper()
minuscula = cad1.lower()

#Primera letra en mayuscula
prim_letra_mayus = cad1.capitalize()

#comando find
buscar_find = cad1.find("f")


print(buscar_find)