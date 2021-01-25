# INICIO DE PRGRAMA ADIVINA EL N°#
while True:
    print("Ingresa ('s') para JUGAR o ('n') para SALIR DEL JUEGO")
    juego_nuevo = input(">>")
#  EMPIEZAN LOS CONDICIONALES PARA COMPARAR#
    if juego_nuevo == "s":
        import random
        chances = 3
        limite = 15
        adivina = random.randint (1,limite)
        nombre = input("como te llamas?" "\n")
        print("-------O--------") 
        print("-------O--------")
        print("HOLA" "\n"+ nombre.upper() + "\n""estas listo para jugar y ganarte un cigarrillo de m$%&@huana armado?")
        print("\n")
        print("-------O--------")
        print("-------O--------")
        print("SOLO TENES QUE ADIVINAR EL NÚMERO ENTRE 1 Y " + str(limite))
        print("\n")
        print ("TENES " + str(chances) + " CHANCES")
        print("\n")
        intentos = 0
        while intentos < chances:
            num = int(input("Ingresa un número" "\n" ">>"))
            if num == adivina:
                    print("GANASTE UN CHARUTO, PEDILE A CACHA QUE TE ARME UNO")
                    print(" (̅_̅_̅(̅__̅l̲̅u̲̅c̲̅k̲̅y̲̲̅̅̅_̅_̅_̅̅()ڪ") 
                    print()
                    break
            elif intentos == chances - 1:
                    print("PERDISTE, TE QUEDAS SIN FUMAR -.-" "\n" "✦Gѧмԑ╰‿╯0ver✦")
                    print("-------O--------")
            elif num > adivina:
                print("PERDISTE UNA CHANCE" "\n" "intenta con un número más chico"  "\n" )
                print("-------O--------") 
            else: 
                print("PERDISTE UNA CHANCE" "\n" "intenta con un número más grande"  "\n" )
                print("-------O--------") 
            intentos += 1 
    elif juego_nuevo == "n": 
        print("CHAO, quedaste CARETOVICH ░°ð°░" "  ""(*-*)../" )
        break
    elif juego_nuevo != "s":
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        print("*-*-*-*-*-DATO INVALIDO*-*-*-*-*-")
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        print()
        print("OPCIONES:---->" "'s/n'" '(minúscula)' "\n" ">>")
    else:
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        print("*-*-*-*-*-DATO INVALIDO*-*-*-*-*-")
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        print()
        print("OPCIONES:---->" "s/n" '(minúscula)' "\n" ">>")