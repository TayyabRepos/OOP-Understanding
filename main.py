#Inheritance
class User():
    def Sign_In(self):
        print('Logged In')

class Lizard(User):
    pass
class Archer(User):
    pass

Archer1 = Archer()
Archer1.Sign_In()