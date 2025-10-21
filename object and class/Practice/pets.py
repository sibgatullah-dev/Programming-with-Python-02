class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def show(self):
        print(f"This is {self.name}. He is {self.age} years old")
        
    def speak(self):
        print("I will get overridden what gives?")

class Cat(Pet):# Inheritance
    
    def __init__(self, name, age,color):
        super().__init__(name, age)
        self.color = color
    
    def speak(self):# Overriding
        print("Meow")
        
    def show(self):
        print(f"This is {self.name}. He is {self.age} years old. His color is {self.color}")
        
class Dog(Pet):
    def speak(self):
        print('Bark')
        
p = Pet( 'Jhon', 21)
p.speak()
p.show()

c = Cat('Larry',3,'brown')
c.speak()
c.show()

d = Dog('Bully',4)
d.speak()
d.show()