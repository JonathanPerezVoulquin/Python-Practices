# LISTAS Y BUCLES FOR 
dates =[[1,2,3,4],
		['a','b','c','d'],
		[5,6,7,8],
		['e','f','g','h'],
		[9,10,11,12],
		['i','j','k','l'],
		[13,14,15,16],	
		['m','n','ñ','o']]

for i in range(len(dates)):	 		
	for j in range(len(dates[i])):
		print(dates[i][j], end="")
	print()

"""
#Recorriendo un string
for i in "artefacto":
	print(i)
print()

#recorriendo un array
for n in [1,2,3,4,5]:
	print(n)
print()

#Recorriendo un diccionario 
for dia in {"lun:lunes", "mar:martes", "mier:miércoles"}:	
	print(dia)
print()	


#MOSTRAR INTERVALOS DE N° ENTRE 1 Y 10
for i in range(1,11):
	print(i)
"""


#TAREA
"""
PROGRAMA QUE VA MOSTRANDO EN UNA CUENTRA ATRÁS LOS NÚMEROS DEL 10 AL 0.
UTILIZANDO UN BUCLE FOR
"""

"""
for i in range(10, -1, -1):
	print(i)


#OTRA FORMA 
for i in range(11):	
	print (10 - i)
"""


#CON BUCLE WHILE
"""
i = 10 
while i >= 0:
	print(i)
	i -= 1

#
"""




#MUY BUENO.
#PROGRAMA QUE TE PIDE 5 NÚMEROS ITERANDO CON EL BÚCLE FOR Y TE DEVUELVE LA SUMA DE LOS MISMOS 

suma = 0
for i in range(5): 
	n = float(input("dime un número:"))
	suma += n
print('la suma es:', suma)
print('gracias por utilizar nuestra apliación')




#TAREA
#Programa que va pidiendo números y los va sumando hasta que alcanza 100 o más

"""
suma = 0 
while suma < 100:
	num = int(input("ingresa un número"))
	suma += num
print("a llegado al número máximo para sumar, su resultado es:",suma)	

"""

# recorriendo listas para encontrar una letra:

letras = ["f","g","h","j","l","m","p","s"]
"""
#PARA HACERLO CON CONDICIONALES, PERO ALGUNOS LENGUAJES NO RECONOCEN EL OPERADOR IN
#ENTONCES SE ÚTILIZA PREFERENTEMENTE EL BUCLE FOR
if "k" in letras:
	print("la letra se encuentra dentro de la lista")
else: 	
	print("La letra no se encuentra dentro de la lista")
"""

#CON BUCLE FOR
encontrado = False
for i in letras:
	if i == "f":
		encontrado = True
if encontrado == True:
	print("la letra está")
else:	
	print("la letra no está")

"""
PROGRAMA QUE PIDE UN NÚMERO AL USUARIO. SI ESE NÚMERO MÁS ALGÚN NUMERO DE LA LISTA
DADA ES IGUAL A 100, EL PROGRAMA DICE QUE EL NÚMERO CUMPLE LA CONDICIÓN

"""

lista = [28,36,43,52,61,75,84,97]
num = int(input("ingresa un número\n"))
encontrado = False
for e in lista:
	if num + e == 100:
		encontrado = True

if encontrado == True:
	print("El número suma 100!! sumando el número elegído, a uno de la lista ")

else:	
	print("El número no cumple la condición")

#el tercer párametro hace que imprima desde el 2 al 6 de 2 en 2 
print(lista[2:6:2])
print(len(lista))