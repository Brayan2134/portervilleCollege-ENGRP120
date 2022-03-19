import turtle
import math

turtle.shape('turtle')
turtle.speed(0)
turtle.bgcolor('black')
turtle.color('white')

def makeHouse():
    for i in range(0,3,1):
        turtle.forward(100)
        turtle.left(120)

def makeLegs():
    turtle.forward(10)
    turtle.right(90)

    for i in range(0,3,1):
        turtle.forward(80)
        turtle.left(90)

def main():
    makeHouse()
    makeLegs()


def coolMain():
    for i in range(30):
        turtle.circle(5*i)
        turtle.circle(-5*i)
        turtle.left(i)
    turtle.exitonclick()

def superMain():
    end_point = int(1000)

    for t in range(0, end_point, 1):
        x = (3+t)*math.cos(t + 0.2) # Type Float
        y = (3+t)*math.sin(t + 0.4) # Type Float
        turtle.goto(x,y)

superMain()
