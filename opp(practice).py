class myCat():
    def __init__(self,name, age, colour):
        self.name = name
        self.age = age
        self.colour = colour

    def __str__(self):
        return f"He is my cat, his name is  {self.name}, it has {self.age} years " \
               f"hair color:{self.colour}"
    #methods within the same class
    def running_fast(self):
        print(f"{self.name} runs very fast")

    def runnig_slow(self):
        print(f"{self.name} runs very slow" )
    def bark_slowly(self):
        print(f"{self.name}, bark slowly")
    def bark_strong(self):
        print(f"{self.name}, bark strong")

myCat1 = myCat("Julieta", "5", "white")
print(myCat1)



class Dog():
    def __init__(self, race, age, colour):
        self.race = race
        self.age = age
        self.colour = colour
    def __str__(self):
        return f"la raza de mi perro es:{self.race} , tiene: {self.age},y el color de su pelo es:{self.colour}"

myDog1 = Dog("caniche", "9", "white")
print(myDog1)
print("la raza de mi perro es", myDog1.race)


