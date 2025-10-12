class car:
    name = ''# This is called class attribute
    color = ''
    
    def __init__(self,n,c):
        self.name = n # This object i created it's name attribute
        self.color = c # this is object attribute or Instance attribute
        
    def start(self):
        print("Starting the engine")
        
my_car = car('Crown','silver') # object created
print(my_car.name)
print(my_car.color)

my_car.start()