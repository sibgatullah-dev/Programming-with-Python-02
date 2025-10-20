class Vehicle:
    def __init__(self,name,manufacturer,color):
        print("Creating a Vehicle")
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
       
class Car(Vehicle) :
    '''Child Class'''
    def __init__(self, name, manufacturer, color,year):
        print("Creating a Car")
        super().__init__(name, manufacturer, color) # calling the available parent constructors . so i don't have to make them self.something
        self.year = year
        self.wheels = 4
        
class MotorCycle(Vehicle):
    def __init__(self, name, manufacturer, color,year):
        super().__init__(name, manufacturer, color)
        self.year = year
        self.wheels = 2
        
if __name__ == "__main__":
    c = Car('Chaser','Toyota','Blue',1998)
    m = MotorCycle('Gixer','Yamaha','Yellow',2016)
    print(c.name,c.manufacturer,c.color,c.year,c.wheels)
    print(m.name,m.manufacturer,m.color,m.year,m.wheels)