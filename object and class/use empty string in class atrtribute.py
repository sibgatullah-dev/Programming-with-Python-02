class car:
    name = "" # used empty string to take an input
    color = ''
    
    def start():
        print("Sarting the engine")
        
car.name = 'BMW'
car.color = 'Blue'

print("Name of the car is :" , car.name)
print("Color of the car is :" , car.color)

car.start()

print(dir(car))