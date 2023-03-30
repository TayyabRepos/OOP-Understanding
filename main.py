class player: #Class
    membership = True #Class Attribute
    def __init__(self, name='Tayyab', age=20): #Constructor
        if(player.membership):
            self.name = name #Attribute
            self.age = age #Attribute
    
    def info(self): #Method
        print(f'Player {self.name} has age of {self.age}')
    @classmethod #Decorator we can access class attribute using cls keyword
    def adding_things(cls, num1, num2):
        return cls(num1 + num2)

    @staticmethod
    def add_things2(num1, num2):
        return num1 + num2

player3 = player.adding_things(2, 3) #@classmethod
player4 = player.add_things2(2, 3) #@staticmethod
print(player3.age)
print(player4)

# player1 = player("Tayyab", 20) #Object
#
# player1.info() #Method
