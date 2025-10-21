class Person:
    number_of_person = 0 # This is a Class Attribute which isn't under any methods
    GRAVITY = -9.8 # If we want to take any constant value we can take it as class attribute
    
    def __init__(self,name):# self represents the instance or obj in normal method
        self.name = name
        Person.add_person()
        
    @classmethod # This is a decorator
    def number_of_people(cls):# This is a class method
        return cls.number_of_person
    
    @classmethod
    def add_person(cls):# cls represents the class 
        Person.number_of_person += 1

if __name__ == '__main__':
    p1 = Person('jim')
    p1 = Person('kelly')
    p1 = Person('Aby')
    print(Person.number_of_people())