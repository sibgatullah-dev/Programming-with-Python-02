class vehicles:
    '''Base class or parent class for all vehicles <- (this is called docstring)'''
    def __init__(self,name,manufacture,color):
        self.name = name
        self.manufacture = manufacture
        self.color = color
        
    def drive(self):
        print('Driving',self.manufacture,self.name)
    def turn(self,direction):
        print('Turning',self.name,'to',direction)
    def brake(self):
        print(self.name,"Stopping")
        
    
#Inheritance
class Car(vehicles):# Creating a class called Car which is inheriting vehicles class
    '''Car Class'''
    def change_gear(self,gear_name):
        '''Method for changing gear'''
        print(self.name,'is changing gear to',gear_name)
        
if __name__ == "__main__":
    v1 = Car("Fusion 110EX",'Walton','Black') # Object one
    v2 = Car("Hino Super 1J",'Hino','Red') # Object two
    v3 = Car("Supra",'Toyota','Blue') # Object three
    
    v1.drive()
    v2.drive()
    v3.drive()

    v1.turn('left')
    v2.turn('right')
    
    v2.change_gear('P')

    v1.brake()
    v2.brake()

    v3.change_gear(3)