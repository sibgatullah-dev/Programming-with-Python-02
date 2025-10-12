class car:
    def __init__(self,name,manufacturer,color,year,cc):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year = year
        self.cc = cc 
        
    def start(self):
        print(f"{self.name} is starting")
    def brake(self):
        print(f"{self.name} is breaking")
    def drive(self):
        print(f"{self.name} is driving")
    def turn(self,direction):
        print(f"{self.name} is turning {direction}")
    def change_gear(self,gear):
        print(f"{self.name} is changing gear to {gear}")
        
Car = car('Chaser','Toyota','Green',1998,1500)

Car.start()
Car.brake()
Car.drive()
Car.turn('Right')
Car.change_gear(3)