import turtle

turtle.shape('turtle')

coolColors = ["red", "green", "blue"]

nodes = eval(input("How many sides of a shape would you like?"))

for i in range (nodes):
    turtle.forward(10)
    for j in range (len(coolColors)):
        turtle.color(coolColors[j])
        turtle.left(176 / nodes)