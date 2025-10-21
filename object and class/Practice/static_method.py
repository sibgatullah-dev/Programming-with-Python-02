# A static method is a function that we normally use outside of a class but put it in a class to organize them 
# A static method doesn't take any (cls) class or (self) instance as they are just regular functions 

class Math:
    
    @staticmethod # Decorator for static method
    def add(x,y):
        return x+y
    
    @staticmethod
    def multi(x,y):
        return x*y
    
    
print(Math.add(5,5))
print(Math.multi(5,4))