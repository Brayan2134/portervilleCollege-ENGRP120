import turtle as turtle


def main():
    numOfSides = eval(input("Please enter number of sides of a polygon you wish to draw!: "))
    
    angleOfSides = 360/numOfSides # Find the interior angle of each side

    for i in range(0, numOfSides,1): # Make polyogon depending on num of sides 
        turtle.forward(100)
        turtle.left(angleOfSides)

    turtle.exitonclick()

#---------------------------------------
if __name__ == "__main__":
    main()
