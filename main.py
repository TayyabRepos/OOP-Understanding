#Encapsulation
class player: #Class
    membership = True #Class Attribute
    def __init__(self, name='Tayyab', age=20): #Constructor
        if(player.membership):
            self.name = name #Attribute
            self.age = age #Attribute

    def info(self): #Method
        print(f'Player {self.name} has age of {self.age}')



player1= player()

player1.info() #Info is the encapsulated method of player class

'Hello World'.capitalize() #Capitalize is the encapsulated method of string class