class myDog():
    def __init__(self,name, age, race, colour, weight):
        self.name = name
        self.age = age
        self.race = race
        self.colour = colour
        self.weight = weight
    def __str__(self):
        return f"He is a dog, his name is  {self.name}, it has {self.age} years " \
               f"his race is {self.race}" \
               f"hair color:{self.colour}, and weighs:{self.weight}"
    #methods within the same class
    def running_fast(self):
        print(f"{self.name} runs very fast")

    def runnig_slow(self):
        print(f"{self.name} runs very slow" )
    def bark_slowly(self):
        print(f"{self.name}, bark slowly")
    def bark_strong(self):
        print(f"{self.name}, bark strong")


myDog1 = myDog("aquiles","13","Schnauzer","black","38kg")
print(myDog1)

myDog2 = myDog("Dylan","5", "toy", "white", "15 kg")
print(myDog2)
print("My dog Aquiles, is of race:",myDog1.race)
print("Dylan:","My other pet is", myDog2.colour)


