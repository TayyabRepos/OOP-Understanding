#Public and private
#@property @name.setter decorator for protected
#__ for private variable, method and class
class player: #Class
    __membership = True # Private Class Attribute
    def __init__(self, name='Tayyab', age=20): #Constructor
        if(player.__membership):

            self._name = name #Attribute
            self._age = age #Attribute

    def __info(self): #Method
        print(f'Player {self._name} has age of {self._age}')

pl1 = player()
pl1._age = 33

print(pl1.info())

