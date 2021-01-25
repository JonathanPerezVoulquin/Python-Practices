caracter = "?"

def encriptador(frase):
	encriptada = ""
	for letra in frase:
		if letra in "aeiouAEIOUáéíóúÁÉÍÓÚ":
			if letra.isupper():
			    encriptada = encriptada + caracter.upper()
			else:    
				encriptada = encriptada + caracter
		else:	
			encriptada = encriptada + letra
	return encriptada	
	


while True:
	print(encriptador(input("Ingresa una frase para encriptar\n")))
	print("Ingresa (1) para encriptar otra frase")
	print("Ingresa (2) para terminar")
	op = input(">")

	if op == "2":
		print("Hasta la próxima")
		break

	

