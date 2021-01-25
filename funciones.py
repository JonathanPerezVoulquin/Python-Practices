#MI PRIMER FUNCIÓN

def saludar():
	print("hola")


saludar()

def numeros(num1,num2):
	
	print("La suma de tus numeros es:" + str( num1 + num2) + "\n""GRACIAS POR UTILIZAR NUESTRO PROGRAMA PYTHON")

numeros(2,5)	


###FUNCIÓN LAMBDA las funciones lamba sirven cuando necesitamos utilizar una sola expresión
resultado = lambda numero: (numero + 40)
print(resultado(30))

### otra función
def numeros ():
	num1 = int(input("Ingresa un número:"))
	num2 = int(input("Ingresa un número que quieras multiplicar:"))	
	num3 = int(input("Ingresa un número que quieras sumar"))
	print ("el resultado que buscas es:"+"\n" + str(num1 * num2 + num3) + "\n""GRACIAS POR UTILIZAR NUESTRO PROGRAMA (:")

numeros()


#FUNCIÓN LAMBDA PARA SUMAR
resultado = lambda numero: (numero + int(input("ingresa un numero:")))
print(resultado(int(input("ingresa un numero que quieras sumar:"))))