# Creating and using a Non-Local variable

def outer():        #outer = externa
    x = "local"

    def inner():        #inner = interna
        nonlocal x              #Nonlocal variable are used in nested fuction(función anidada)
        x = "nonlocal"
        print("inner:",x)

    inner()
    print("outer:",x)
outer()

#NINGUNA DE LAS 2 VARIABLES SON LOCALES "nonlocal"
