# Global and Local variable with different name
x = "global"  # Global variable can be accesed from anywhere


def fuct1():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)


print("Esto es una variable global")
print(x)
print("---------0-----------")
print(fuct1())
print("Global x =", x)

# Global and local variable with same name (with same name= con mismo nombre)
