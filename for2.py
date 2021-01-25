lista = [	"Abril",
			"Julian",
			"Maite",
			"Miguel",
			"Eulogía",
			"Joaquin"]

nombre_usuario = "Miguel"

for n in range(len(lista)):
	if lista[n] == nombre_usuario:
		print("el nombre de usuario",nombre_usuario.upper(), "aparece en la lista en el indice", n )

lista.insert(1,"Pepe Lui")
print(lista)		


frutas = ['Pera','Manzana','Sandia']

lista.extend(frutas)
print(lista)

"""
encontrado = 8
for i in range(10,-1,-1):
	print(i)
	if encontrado == i:
		print("el número se encuentra en la lista en la posición:", i)
"""