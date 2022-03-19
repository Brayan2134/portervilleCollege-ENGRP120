import turtle
import random

turtle.shape('turtle')
turtle.speed(0)
turtle.bgcolor('black')


"""#Making a triangle
for x in range(1,4,1):
    turtle.forward(100)
    turtle.right(120)
"""

"""#Making a kite
turtle.left(60)
for i in range(1,5,1):
    turtle.forward(100)
    turtle.left(90)"""

colors = ['red', 'yellow', 'green', 'blue', 'white']

def makeSquare():
    for i in range(0,4,1):
        turtle.left(90)
        turtle.forward(200)

def changePenColor():
    lenColors = len(colors)
    r1 = random.randint(0, (lenColors - 1))
    turtle.pencolor(colors[r1])


#Make a cool circle thing!
for x in range(0,100,1):
    changePenColor()
    makeSquare()
    turtle.right(35)
