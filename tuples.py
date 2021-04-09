#tuples are immutable!!! IMPORTANT
# creating an empty tuple
tuple1 = ()
print(tuple1)

#creating tuples with integer elements
tuple2 = (1,2,3)
print(tuple2)

#tuple with mixed datatyes
tuple3 = (101,"Anirban", 20000.00,"HR Dept")
print(tuple3)

#creation of nested(anidada) tuple
tuple4 = ("points",
          [1,2,3],
          [7,8,9],
)
print(tuple4)
#tuple can be created without any parentheses
#also called tuple packing
tuple5= 101,"Anirban", 20000.00,"HR dept"
print(tuple5)

#tuple unpacking is also possible(item for item)
empid, empname, empsal, empdept= tuple5
print(empname)
print(empsal)
print(empdept)
print()
print("----o-----")
print("the size of the tuple is")
print(len(tuple5))
print()
print("----o-----")
"""
"""
#accesing elemets in a tuple
tuple6 = ('w','e','l','c','o',"m","e")
print(tuple6)
print(tuple6[0])
print(tuple6[6])
print(tuple6[-1])
print(tuple6[-7])
"""
"""
# accesing elements in nested tuple (tuplas anidadas)
nestedTuple = (
    "point",
    [6,7,8],
    (12,14,16)
)
print(nestedTuple)
print(nestedTuple[1]) #[6,7,8]
print(nestedTuple[0]) # "point"
print(nestedTuple[2][2]) #16
print("----o-----")

# slicing tuple contents (decir de donde a donde se imprime)
tuple7 = ("H","E","L","O", "W","O","R","L","D")
print(tuple7)
print(tuple7[1:4])
print(tuple7[-5:])
print(tuple7[-5:-2])

print("----o-----")
# concatenation of tuples
tuple8 = ("w","e","l")
tuple9 = ("c","o","m","e")
print(tuple8 + tuple9) # welcome
print(tuple9)
print(tuple9[0:2])
print(tuple9[2:])