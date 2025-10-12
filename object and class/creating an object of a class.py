class car:
    name=''
    color=''
    
    def start(self): # when we call a method of an object that object goes in the method function to stop this we need to use self
        print('Starting the engine')

# creating a car object
my_car = car() # Instantiate
my_car.name = 'Crown'
my_car.color = "Silver"
print(my_car.name)
my_car.start()