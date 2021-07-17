class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def __str__(self):		#
		return f"Hi, i'am {self.name}, i have {self.age} years"
	def student(self):		#method
		print(f"{self.name}, study programming")

class Dog_class:
	def __init__(self, name ,race ,age):
		self.name = name
		self.race = race
		self.age = age
	def bark(self):
		print(f"My dog it is a dog of {self.race} race and barks loudly. His name is{self.name} achilles. your age is {self.age}  ")
person1 = Person("Jonathan", "27")
print(person1)
person1.student()
print(person1.age)
dog1 = Dog_class('Aquiles', 'Schnawzer','13')
dog2 = Dog_class('José','PoliceAleman','23')

print(dog1.bark())
print(dog1.name)
print(dog1.bark())

print(type(dog2.race + dog2.bark()))

