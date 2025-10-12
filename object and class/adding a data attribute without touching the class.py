class car:
    def __init__(self,name,color):
        self.name = name
        self.color = color
        
    def start(self):
        print("starting the engine")
        
car1 = car("Crown","Silver")
car1.year = 2024

print(car1.name,car1.color,car1.year)
car1.start()