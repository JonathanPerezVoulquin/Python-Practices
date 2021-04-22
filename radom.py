import random

a = random.randint(1,10)
print(a)

b = random.normalvariate(0,1)
print(b)

myList = ['a','b','d']
c = random.choice(myList)
print(c)

#otra forma de codificarlo sería mediante la funcion list()
myList2 = list("ABCDEFGHI")
d = random.choice(myList2)
print(d)

#imprime los elementos ordenados al azar
myList3 = list("JON")
random.shuffle(myList3)
print(myList3)
"""
random.seed(1)
print(random.random())
print(random.randint(1,10))
random.seed(2)
print(random.random())
print(random.randint(1,10))

random.seed(1)
print(random.random())
print(random.randint(1,10))

random.seed(2)
print(random.random())
print(random.randint(1,10))
"""

#Seleccionar un Super Heroe con funcion random.choice() y pasandole como parametro la lista
superHero = [
    "IronMan",
    "Capitan America",
    "Black Widow",
    "Dr Strange",
    "Thor",
    "Hulk",
    "Spiderman",
]

sH = random.choice(superHero)
print(sH)

g = random.randint(1,10)
print(g)
