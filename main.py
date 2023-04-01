#Polymorphism 
#Overloading
#OverRiding

class A():
    def Area(self, a=None, b=None):
        if(a!=None and b!=None):
            print(a*b)
        elif(a!=None):
            print(a*a)
        else:
            print("Nothing to find")

class B(A):
    def Area(self):
        super().Area() #To call function form parent class
        print("Area form B")

objA = A()
  
objA.Area() #Overloading
objA.Area(10) #Overloading
objA.Area(10,20) #Overloading

objB = B()
objB.Area()