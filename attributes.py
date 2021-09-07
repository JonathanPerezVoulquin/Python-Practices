"""
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
user1 = User('joni', 'xasdqw')

user1.permision = True          #acá agregamos atributos que no están en la clase
user1.admin = False

print(user1.username)
print(user1.password)
print(user1.permision)
print(user1.__dict__)           #dictonary

"""


# Para restringir agregar atributos como en el ejemplo de arriba con __slots__
class User:
    __slots__ = ['username', 'password']

    def __init__(self, username, password):
        self.username = username
        self.password = password


class Students(User):
    pass

user1 = User('joni', '23654')
print(user1.username)
print(user1.password)

# print(user1.__dict__) ya no se puede usar el atributo .__dict__ porque restringimos los atributos en la clase

class Course(User):
    def __init__(self,lenguage, level, id_student):
        self.lenguage = lenguage
        self.level= level
        self.id_student = id_student

id_user1 = Course('python', 'intermediate', 32)
id_user1.permision = True
id_user1.password = '123123123'
print(id_user1.password)
print(id_user1.__dict__)
