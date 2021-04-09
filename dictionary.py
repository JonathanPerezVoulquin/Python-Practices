#Accesing elements from a dictionary
from typing import Dict

new_dictonary: dict[int, str] = {
                 1:"Hello",
                 2:"Hi",
                 3:"Hola",
                 4: "Bonjour"
}
print(new_dictonary)
print(new_dictonary.get(2))  #using get tu print the value of the key

# Updating value (actualizar un valor)
new_dictonary[1]= "Hey You"
print(new_dictonary)

#Adding value (agregar un valor nuevo)
new_dictonary[5] = "Namaste"
print(new_dictonary)
print("--------0----------")

# Creating a new dictionary
squares: dict[int, int] = {
    1:1,
    2:4,
    3:9,
    4:16,
    5:24
}
print(squares)
print(squares.pop(4))  #delete the indicated value
print(squares)  #(delete indicated value)

#remove an arbitrary item
print(squares.popitem())
print(squares)

#delete a particular item
del squares[3]
print(squares)
squares[6] = 12
print(squares)

del squares[1]
print(squares)
print((squares.get(2)))
print(len(squares))
print(type(squares))
print()
print("----------0------------")

