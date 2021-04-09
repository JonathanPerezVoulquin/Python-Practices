# Global and local variable with same name (with same name = con el mismo nombre)
a = 5


def funct1():       #se accede a la variable local desde esta función por más que se llamen igual
    a = 10         # local variables are accessed from the block  where it is defined only
    print("local a:", a)


print("global a:", a)
funct1()
print("global a:", a)
funct1()
