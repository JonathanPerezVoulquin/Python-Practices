lista = [
		28,
		36,
		43,
		44,
		52,
		61,
		43,
		84,
		87,
		43,
		97			
]

numero = 43
contador = 0

for e in lista:
	if e == numero:
		contador += 1
print('el número', numero, 'esta', contador, 'veces')



"""
#TAREA
Tenemos una tupla con los meses del año. Queremos saber qué meses tienen en su nombre la letra "b"
"""

meses = ("Enero", "Febrero", "marzo",
		 "Abril", "Mayo", "Junio",
		 "Julio", "Agosto", "Septiembre",
		 "Octubre","Noviembre","diciembre")

for m in meses:
	if "b" in m:
		print("El mes de", m, "tiene la letra b")


"""
#TAREA
Programa que compruebe si un elemento está en una lista 
y nos indique en que posición (de índice) se encuentra
"""

list_num = [2,5,90,23,45,87,54,11,38]

element = 54

for i in  range(len(list_num)):
	if list_num[i] == element:
		print("el", element, "esta en la posición",i + 1)#se pone el +1 para marcar la posición, no el índice


for e in range(10, -1, -1):
	print(e)