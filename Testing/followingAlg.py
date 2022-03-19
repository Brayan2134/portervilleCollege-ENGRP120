import turtle as turtle
import math
import random

def main():
    turtle.penup()
    
    # Initial Value of where turtle is
    init_x = random.randint(-300,300)
    init_y = random.randint(-300,300)
    print("Initial: ", "x-cord: ", init_x, " y-cord: ", init_y)

    # Randomly choose where the ending value of turtle
    twox = random.randint(-300,300)
    twoy = random.randint(-300,300)
    print("Max Distance: ", "x-cord: ",twox, " y-cord: ", twoy)

    # Find (Triangle) Delta x, Delta y, and hypotnuse for points selected
    x_dist = twox - init_x
    y_dist = twoy - init_y
    r_dist = int(math.sqrt((x_dist ** 2) + (y_dist ** 2)))

    print("x-distance: ",x_dist, " y-distance: ",y_dist, " hypotnuse: ", r_dist)
        
    # Quadrent 1: X_dist, Y_dist are positive
    if (x_dist > 0) & (y_dist > 0):
        for z in range(init_x, x_dist, 1): # 3rd arg is how percise you wish graph to be!
            if z == 0: # Prevent div by 0 error
                z = 1

            # Prevent Vertical line from forming
            turtle.pendown()

            midpoint = r_dist / z
            turtle.goto(z, midpoint)

    # Quadrent 2: x_dist negative, y_dist poisitve
    if (x_dist < 0) & (y_dist > 0):
        for z in range(x_dist, init_x, 1):
            if z == 0:
                z = 1
            
            turtle.pendown()

            midpoint = r_dist / abs(z)
            turtle.goto(z, midpoint)

    # Quadrent 3: x_dist, y_dist are negative
    if (x_dist < 0) & (y_dist < 0):
        for z in range(x_dist, init_x, 1):
            if z == 0:
                z = 1

            turtle.pendown()
            
            midpoint = r_dist / z
            turtle.goto(z, midpoint)

    # Quadrent 4: x_dist positive, y_dist negative
    if (x_dist > 0) & (y_dist < 0):
        for z in range(init_x, x_dist, 1):
            if z == 0:
                z = 1
            
            turtle.pendown()
            
            midpoint = r_dist / (z * -1)
            turtle.goto(z, midpoint)

    turtle.exitonclick()
main()