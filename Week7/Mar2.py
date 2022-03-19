"""
    Name: Brayan Quevedo Ramos
    Initial Commit Date: 2, March 2022

    Purpose: To make a house!
"""

import turtle as turtle
import math

def main():
    #top of house
    for i in range(0,3,1):
        turtle.forward(100)
        turtle.left(120)
    
    turtle.right(90)

    #Left of hosue
    for x in range(0,2,1):
        turtle.forward(100)
        turtle.left(90)

    #line
    turtle.forward(100)
    turtle.right(225)
    turtle.forward(140)

    #line
    turtle.right(135)
    turtle.forward(100)
    turtle.right(135)
    turtle.forward(140)

def hello():
    turtle.exitonclick()

def perpMain():
    end_point = int(1000)

    for t in range(0, end_point, 1):
        x = (16)*math.sin(t) ** 3
        y = (13)*math.cos(t) - (5)*math.cos(2*t) - (2)*math.cos(3*t)-math.cos(4*t)
        turtle.goto(x,y)


if __name__ == "__main__":
    #hello()
    #main()
    perpMain()