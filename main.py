import turtle
import random
turtle.bgcolor("black")
bob=turtle.Turtle()
bob.speed(100)
bob.pensize()
for pos in range(150):
    bob.color("red")
    bob.circle(pos)
    bob.left(130)

turtle.colormode(255)
bob = turtle.Turtle()
bob.speed(0)
for x in range(120):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    myColor=(r,g,b)
    mySize=(x*0.2)
    mySide=random.randint(5,10)
    bob.forward(x *0)
    bob.left(30)
    
 
