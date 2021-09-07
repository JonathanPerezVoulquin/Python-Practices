import random

adivina = random.randint (1,6)

nombre = input("como te llamas?" "\n")
print("Hola" "\n"+ nombre.upper() + "\n""estas listo para jugar y ganar?")
print ("Solo tenes 3 posibilidades")

#Acá se declara la primer chance y la variable n°
num = int(input("intenta adivinar, elige un n° del 1 al 12:" "\n"))

if num == adivina:
	print("GANASTE UN CHOCOLATE")
	print("Decile a cacha que te haga 'UOOO'")	
else:
	if num != adivina:
		print("Perdiste 1 chance, te quedan 2")


	#Acá se declara la segunda chance, y se define nuevamente la variable n°
	num = int(input("intenta adivinar, elige un n° del 1 al 12:" "\n"))

	if num == adivina:
		print("FELICITACIONES, GANASTE UN CHOCOLATE")
		print("Decile a cacha que te haga 'UOOO'")	
	else:
		if num != adivina:
			print("Perdiste 2 chances, te quedan 1")

		#Acá se declara la última chance y se define nuevamente la variable n°
		num = int(input("Última oportunidad:" "\n"))

		if num == adivina:
			print("FELICITACIONES, GANASTE UN CHOCOLATE")
			print("Decile a cacha que te haga 'UOOO'")	
		else:
			if num != adivina:
				print("PERDISTE,TE QUEDAS SIN FUMAR, " + nombre.upper() )
