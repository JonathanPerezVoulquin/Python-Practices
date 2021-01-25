def sumar (a,b):
	return a + b

def restar (a,b):	
	return a - b

def multiplicar(a,b):	
	return a * b 

def dividir (a,b):	
	return a / b


#Acá empieza el programa "calculadora 3.0 con bucle infinito y break, by Jonathan Perez"

def menu():	
	print("1 para sumar")
	print("2 para restar")
	print("3 para multiplicar")
	print("4 para dividir")
	op = input("elige operación:" "\n" ">>")
	return op


n1 = float(input("introduce un numero" "\n" ">>"))


while True:

	op = menu()

	n2 = float(input("introduce otro número" "\n" ">>"))

	if op == "1":
		resultado = sumar(n1,n2)
	elif op == "2":
		resultado = restar(n1,n2)
	elif op == "3":
		resultado = multiplicar(n1,n2)
	elif op == "4":				
		resultado = dividir(n1,n2)
		

	n1 = resultado 	
	print("el resultado es:" "\n" ">>", resultado)

	seguir = input("desea seguir operando con este mismo número? s/n, otro" "\n" ">>")

	if seguir == "n":
		print("Gracias por utilizar nuestro programa 'By Jonathan Perez'".upper())			
		break

#hasta acá es el primer ciclo infinito y el programa funciona bien/ y empieza el que me trae problemas para que termine lpm..
    
	elif seguir == "otro":
		n1 = float(input("ingresa un nuevo número" "\n" ">>"))


#ACÁ LO SOLUCIONE:cambie el segundo while de 'True' a 'False' no entiendo bien que paso, pero logré que el programa terminara, estudiarlo más y entender el porque.
		while False:

			op = menu()

			n2 = float(input("ingresa otro número" "\n" ">>"))

			if op == "1":
				resultado = sumar(n1,n2)
			elif op == "2":
				resultado = restar(n1,n2)
			elif op == "3":
				resultado = multiplicar(n1,n2)
			elif op == "4":				
				resultado = dividir(n1,n2)	

			n1 = resultado
			
			print("el resultado es:" "\n" ">>", resultado)

			seguir = input("desea seguir operando con el mismo número, 'n' para finalizar.? 's/n, otro'" "\n" ">>")

			if seguir == "n":
				break 		
				

