import turtle

class AjobTurtle(turtle.Turtle):
    def forward(self, distance):
        super().backward(distance)
    def backward(self,distance):
        super().forward(distance)
    def left(self,angle):
        super().right(angle)
    def right(self,angle):
        print("I won't turn right hump....")
        
if __name__ == "__main__":
    montu = AjobTurtle()
    montu.left(30)
    montu.forward(200)
    montu.left(45)
    montu.backward(100)
    montu.right(90)
    montu.forward(30)
    
    jhontu = turtle.Turtle()
    jhontu.shape('turtle')
    jhontu.left(30)
    jhontu.forward(200)
    jhontu.left(45)
    jhontu.backward(100)
    jhontu.right(90)
    jhontu.forward(30)
    
    turtle.done()