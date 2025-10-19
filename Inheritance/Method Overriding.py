''' method overriding is a concept where a subclass provides a different implementation of a method
  which is already defined in it's parent class method '''
  
class Vehicles:
    '''Base class'''
    def __init__(self,name,manufacturer,color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        
    def turn(self,direction):
        print("Turning",self.name,'to',direction)

class Car(Vehicles):
    def __init__(self, name, manufacturer, color,year):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year = year
        
    def change_gear(self,gear):
        print(self.name,'is changing gear to',gear)
        
    def turn(self, direction):# here we are overriding the parent class's method with this one
        print(self.name, 'is turning', direction)
        
if __name__ == '__main__':
    c = Car('Chaser','Toyota','Black',1998) # creating object with child class
    v = Vehicles('GTR',"Nissan",'Blue')# Creating object using parent/base class
    
    c.turn('right') # calling the overriding method from the child class
    v.turn('left') # calling the method from the parent class