class car:
    def __init__(self,n,c): # __init__ is called constructor 
       self.name = n # Here the attribute is being created is called (instance attribute)/ object attribute
       self.color = c
    
    def start(self):
        print("Name: ",self.name)
        print("Color: ",self.color)
        print("Starting the engine")

my_car = car('Chaser','white')
my_car.start()
# if we call the method like this car.start(my_car) it will also work by passing the object in the method 
# but this system isn't appropriate

car1 = car('corolla','gray')
car2 = car('Premio','Black')
car3 = car('Allion','Blue')
car4 = car('Crown','Bronz')
car1.start()
car2.start()
car3.start()
car4.start()