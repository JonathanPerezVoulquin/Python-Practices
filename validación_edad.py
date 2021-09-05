def ingreso_edad (num):
	if num >= 18:
		return True
	else:
		return False
	

nombre = input("Bienvenido, cual es tu nombre?:")

print("Hola" "\n" + nombre)

respuesta = input("Eres Mayor de edad?")
if respuesta == "si":
	print("Cuantos años tienes?")
	edad = input()
	if ingreso_edad (int(edad)):
		print("Eres mayor,disfruta de la vida ")
	else:
		print("LARGO DE AQUÍ, te recomiendo www.barneyeldinosaurio.com")	

else:
	print("No puedes entrar, pero me gusta tu honestidad")	


