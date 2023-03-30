class player: #Class
    membership = True #Class Attribute
    def __init__(self, name, age): #Constructor
        if(player.membership):
            self.name = name #Attribute
            self.age = age #Attribute
    
    def info(self): #Method
        print(f'Player {self.name} has age of {self.age}')

player1 = player("Tayyab", 20) #Object

player1.info() #Method
