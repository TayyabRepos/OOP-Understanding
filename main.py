#Polymorphism
class User():
    def Sign_In(self):
        print('Logged In')

class Lizard(User):
    pass
class Archer(User):
    pass

Archer1 = Archer()
Archer1.Sign_In()

#isinstance(instance , class)

print(isinstance(Archer1, Archer))

print(isinstance(Archer1, User))

print(isinstance(Archer1, object)) # Object by default is parent class for all the class in python