class Vehicles:
    '''Base class for all vehicles'''
    def __init__(self,name,manufacturer,color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        
        def drive(self):
            print('Driving',self.manufacturer,self.name)
        def turn(self,direction):
            print(self.name,'is turning',direction)
        def brake(self):
            print(self.name,'is stopping.')
            
class Car(Vehicles):
    '''car class'''
    def __init__(self, name, manufacturer, color,year):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year = year
        self.wheels = 4
        print('A new car has been created. Name: ',self.name)
        print("It's manufacturer is ",self.manufacturer)
        print('It has',self.wheels,'wheels')
        print('The car was built in',self.year)
        
    def change_gear(self,gear):
        '''Method of changing gear'''
        print(self.name,'is changing gear to',gear)
        

if __name__ == "__main__":
    c = Car('Chaser','Toyota','White',1998)
        
        
        