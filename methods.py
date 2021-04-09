# list
from typing import Union
import random
chekingList = ['Carlos', 'José', 'María', 'klan', 'Micaela', 'Jorge']
print(chekingList)

# .Append()
chekingList.append('Eulogía')
print(chekingList)

# .pop() saca el elemento que le indiquemos de la lista
chekingList.pop(1)
print(chekingList)
chekingList.pop(0)
print(type(chekingList))

list2: list[Union[bool, int, str]] = [True, 24, 'Nuevo alumno:', 'José']
print(list2)

chekingList.extend(list2)
print(chekingList)

chekingList.remove('José')
print(chekingList)

chekingList.pop(2)
print(chekingList)

# clear() limpia toda la lista completa
# chekingList.clear()
print(chekingList)
"""
practices 
"""
"""other practices

Running with "for"

 """
for i in list2:
    print(i)
for i in chekingList:
    print(i)
chekingList.remove(True)
print(chekingList)
"""other practices
 
Running with "for"
 
 """
myListFruit = ['apple','banana','cherry','orange']
myListFruit.append('kiwi')
print(myListFruit)
myListFruit.pop()
print(myListFruit)
myListFruit.pop()
myListFruit.extend(chekingList)
print(myListFruit)
myListFruit.remove(24)
print(myListFruit)
myListFruit.remove('Nuevo alumno:')
print(myListFruit)
myListFruit.pop()
print(myListFruit)
myListFruit.clear()
print(myListFruit)
myListFruit.append('jorgue')
print(myListFruit)


#I ran a random selector, to say your superhero random
superHero = ['Irom man',
             'Batman',
             'Linterna verde',
             'Superman',
             'Sherk',
             'Goku',
             'Gohan',
             'Trunks',
             'Vegeta',
             'Picolo',
             'Spiderman',
             'Aquaman xD',
             'Señor mishagui'
             'Heidy',
             'Señor Barriga',
             'La chilindrina',
             'Chapulin Colorado',
             'El zorro',
             'Dora la exploradora',
             'Rafa gorgori',
             'Oficial gorgori',
             'Mr magoo',
             'El chavo del 8',
             'Quico',
             'Klan',
             'El burro de sherk',
             'Vicente Vinolli',

             ]
tuSuperHero =(random.choice(superHero))
print(tuSuperHero)

# while/ practice
"""
one = 1
while 1 == one:
    num = int(input("ingresa un número:" ">>"))
    suma = str(num + one)
    one = suma
    print(str("tu número + 1 es:" + one))
    break
"""
