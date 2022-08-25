"""
    Name: Brayan Quevedo Ramos
    Initial Commit Date: 28, Febuary 2022

    Purpose: Create a randomly generated image based on initial questions asked to the user.

    Other Pupose: To learn how to use the Python threading library & try/catch

    Notes: Program reading follows Google Python Env. Ruleset (read from bottom to top for appended func)
           https://google.github.io/styleguide/pyguide.html

           FOR MORE DETAILS: https://github.com/Brayan2134/portervilleCollege-ENGRP120
"""


#------------------------------------------------
"""
    PYTHON LIBRARIES REQUIRED FOR PROGRAM TO RUN
"""

import turtle as animal
from threading import Thread
import random
import math
#------------------------------------------------


#------------------------------------------------
"""
    GLOBAL SETTINGS FOR PROGRAM TO RUN

    @Special: userSettings index reference -- 
              [0] = name of user (str)
              [1] = age of user (int)
              [2] = favorite color of user (str)
              [3] = random number (int) from len(user) (a)
              [4] = random number (int) from age of user (x)
              [5] = random number (int) from fav color of user (k)
"""
userSettings = [] # !IMPORTANT: ARRAY THAT STORES WHAT USER INPUT INTO PROGRAM, ARRAY THAT STORES CALCULATIONS (SEE ABOVE)
penColors = ["white", "green", "blue", "orange"] # Available colors that pen color can be!
x = 0 # Initial X coordinate (used to create shapes)
y = 0 # Initial Y coordinate (used to create shapes)
#------------------------------------------------


# Define world boundary settings!
def initSettings():
    animal.bgcolor('black')
    animal.speed(0)


# From welcomeuser() func:
#   @Special: Check to see if what user has input is valid.
#   @Note: Int check has been excluded from func as try/catch must be local NOT called
def checkIfValidInput(userSettings):

    # Check if name inout field is valid
    if (len(userSettings[0]) == 0):
        while (len(userSettings[0]) == 0):
            print("Sorry! put an invalid answer for your name!")
            userSettings[0] = input("What's your Name?:")

    # Check if favcolor input is valid
    if(len(userSettings[2]) == 0):
        while (len(userSettings[2]) == 0):
            print("Sorry! put an invalid answer for your favorite color!")
            userSettings[2] = input("What's your favorite color?:")


# From main()
#   @Special: Welcome user, and ask for basic details. Then Append to array
#   @Note: checkIfValid() EXCLUDED int check; included here
def welcomeUser():
    # User input (will be checked, and used for appendments)
    localStrUserSettings = ""
    localIntUserSettings = 0

    print("\n Hello and welcome to the picture generator!")
    print("I hope you're having a fabulous day!")
    print("I have some questions for you before you have your PERSONALIZED image!")
    
    localStrUserSettings = input("What's your name?: ")
    userSettings.append(localStrUserSettings) # Add to array [0]

    # Check if user input is int
    while True:
        try:
            localIntUserSettings = int(input("What's your age?: "))
            break
        except ValueError:
            print("Sorry! You chose an invalid option. Please try again \n")
            continue

    userSettings.append(localIntUserSettings) # Add to array [1]

    localStrUserSettings = input("What's your favorite color?: ")
    userSettings.append(localStrUserSettings) # Add to Array[2]

    #print(userSettings) # For bug fixing reasons

    checkIfValidInput(userSettings) # Check if what user has is valid


# @ Special: Randomize values from user input. Will be used for param eq.
def setupTrigValueName(userSettings):
    randomIntFromName = random.randint(0, (len(userSettings[0]) - 1))
    userSettings.insert(3, randomIntFromName)


# @ Special: Randomize values from user input. Will be used for param eq.
def setupTrigValueAge(userSettings):
    localAgeFromArray = int(userSettings[1])
    randomIntFromAge = random.randint(0, ((localAgeFromArray * 10) - 1))
    userSettings.insert(4, randomIntFromAge)


# @ Special: Randomize values from user input. Will be used for param eq.
def setupTrigValueFavColor(userSettings):
    localFavColorLenFromArray = len(str(userSettings[2]))
    userSettings.insert(5, (localFavColorLenFromArray * 11))


# Will call all setup__() functions
# @Special: Will be called to completly randomize numbers so every iteration of param loop is unique
def randomizeValues(userSettings):
    setupTrigValueName(userSettings)
    setupTrigValueAge(userSettings)
    setupTrigValueFavColor(userSettings)


# @Special: With each iteration of createParametricEquation(), randomly choose dif. pen color
def changePenSettings():
    lenPenColors = len(penColors) - 1
    changePenColor = random.randint(0, lenPenColors)
    animal.color(penColors[changePenColor])


# @Special: Parametric Equation Algoirthm (1/x on Desmos)
# @Note: INCREASING SCALE OF RANDOM VALUES WILL SLOW DOWN PROGRAM!!!
def createGraph():

    # Initial Values

    # Randomly choose starting x-coord from userSettings, and Random
    init_x = (random.randint(-10,10) + int(userSettings[3])* math.cos(int(userSettings[4])) + int(userSettings[5])) # Change random depending on how "random" you want program to be!
    init_x = init_x ** random.randint(-2,2)
    init_x = round(init_x)
    
    randomizeValues(userSettings) # RE-RANDOMIZE values for initial Y-cord.

    # Randomly choose starting y-coord from userSettings, and Random
    init_y = (random.randint(-10,10) + int(userSettings[3])* math.sin(int(userSettings[4])) + int(userSettings[5]))
    init_y = init_y ** random.randint(-2,2)
    init_y = round(init_y)

    randomizeValues(userSettings)

    print("Initial x-value: ", init_x, " Initial y-value: ", init_y) # Display what init values are

    # Ending values

    # Choose where end point will be
    twox = random.randint(-500,500)
    twoy = random.randint(-500,500)

    print("Final x-value: ", twox, " Final y-value: ", twoy) # Display what final values are

    # CREATE TRIANGLE FROM INIT/FINAL POINTS
    x_dist = twox - init_x # Find \delta x
    y_dist = twoy - init_y # Find \delta y
    r_dist = int(math.sqrt((x_dist ** 2) + (y_dist ** 2))) # Find Hypotnuse (r) that connects \delta x \& \delta y

    print("x-distance: ",x_dist, " y-distance: ",y_dist, " hypotnuse: ", r_dist) # Display \delta cords. and Hypotnuse (r)
    print("")

    """
        HOW ALGO WORKS:
        
        Reqs: Delta x/y and r (three parts required to make a triangle)

        - Given these values, keep in memory what the triangle is.

        - Create curve by finding middle between hypotnuses (r) / bottomline of triangle (depending on cond.)

        Note: in each 'for z' statement, Random.func() call is percisiion of curve

    """
    
    # Quadrent 1: X_dist, Y_dist are positive
    if (x_dist > 0) & (y_dist > 0):
        for z in range(init_x, x_dist, random.randint(1,10)): # 3rd arg is how percise you wish graph to be!
            if z == 0: # Prevent div by 0 error
                z = 1

            animal.pendown()

            midpoint = r_dist / z
            animal.goto(z, midpoint)

    # Quadrent 2: x_dist negative, y_dist poisitve
    if (x_dist < 0) & (y_dist > 0):
        for z in range(x_dist, init_x, random.randint(1,10)):
            if z == 0:
                z = 1
            
            animal.pendown()

            midpoint = r_dist / abs(z)
            animal.goto(z, midpoint)

    # Quadrent 3: x_dist, y_dist are negative
    if (x_dist < 0) & (y_dist < 0):
        for z in range(x_dist, init_x, random.randint(1,10)):
            if z == 0:
                z = 1

            animal.pendown()
            
            midpoint = r_dist / z
            animal.goto(z, midpoint)

    # Quadrent 4: x_dist positive, y_dist negative
    if (x_dist > 0) & (y_dist < 0):
        for z in range(init_x, x_dist, random.randint(1,10)):
            if z == 0:
                z = 1
            
            animal.pendown()
            
            midpoint = r_dist / (z * -1)
            animal.goto(z, midpoint)


# TO BE CALLED ON BY createParam.Eq.()
# @Special: Randomly create one of many shapes
def createShape():
    print("")
    print("You are creating a shape!")
    animal.goto(random.randint(-300,300), random.randint(-300,300)) # Go to random cord. on graph (can be changed)

    # Choose one of 5 pre-selected shapes to make
    goTo = random.randint(1,5)

    if(goTo == 1):
        # Create Square (1)
        print("\t Chosen Shape: Square")
        for x in range(0,4,1):
            animal.forward(100)
            animal.left(90)

    if (goTo == 2):
        # Create Rectangle (2)
        print("\t Chosen Shape: Rectangle")
        for x in range(0,4,1):
            if (x == 0) | (x == 2):
                animal.forward(200)
                animal.right(90)

            animal.forward(random.randint(1,200))
            animal.right(90)

    if (goTo == 3):
        # Create Circle (3)
        print("\t Chosen Shape: Circle")
        radius = random.randint(1,100)
        animal.circle(radius)

    if (goTo == 4):
        # Create triangle
        print("\t Chosen Shape: Triangle")
        for i in range(0,3,1):
            animal.forward(random.randint(1,200))
            animal.left(120)

    
    if (goTo == 5):
        # Create polygon of n sides
        print("\t Chosen Shape: Polygon")
        numOfSides = random.randint(4,15)
        angleOfSides = 360/numOfSides # Find the interior angle of each side

        for i in range(0, numOfSides,1): # Make polyogon depending on num of sides 
            animal.forward(100)
            animal.left(angleOfSides)
    print("")


# @Special: Create everything on graph 
def createParametricEquation(userSettings):
    animal.pencolor(penColors[0])

    for timeOfCreation in range(0, 1000, random.randint(1,6)): # 2nd arg can be changed: (n << init less time creating) and (n >> init more time creating)
        changePenSettings()
        createGraph()
        createShape()

    animal.exitonclick()


# @ Special: Randomize values from user input to create param. eq.
def convertUserInputToTrig(userSettings):
    print("Creating your image...")

    # Set target of three threads
    functionThreadFunc1 = Thread(target = setupTrigValueName(userSettings))
    functionThreadFunc2 = Thread(target = setupTrigValueAge(userSettings))
    functionThreadFunc3 = Thread(target = setupTrigValueFavColor(userSettings))

    # Excecute inputs threads
    functionThreadFunc1.start()
    functionThreadFunc2.start()
    functionThreadFunc3.start()

    print(userSettings)

    # Kill threads (3 --> 0)
    functionThreadFunc1.join()
    functionThreadFunc2.join()
    functionThreadFunc3.join()

    createParametricEquation(userSettings)


# Main program (everything starts from here!)
def main():
    initSettings()
    welcomeUser()
    convertUserInputToTrig(userSettings)

#---------------------------------------
if __name__ == "__main__": # Run as script
    main()