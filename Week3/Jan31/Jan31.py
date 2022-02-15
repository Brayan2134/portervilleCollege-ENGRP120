"""
    Name: Brayan Quevedo Ramos
    Date: 31, Jan, 2022

    Purpose: Convert from C to F
    - Convert from F to C
    - Computing the Average
"""

# Convert to Farenheight from Celsius
    #@args: c (float)
    # c (float): argument to convert from c to f
def convertToF(c):
    cLocal = float(c)
    fOut = (cLocal * (9/5)) + 32
    print("Input: ", cLocal , " celsius. Out: ", fOut, " farenheight")

# Convert to Celsius from Farenheit
    #@args: f (float)
    # f (float): arguemnt to convert from f to c
def convertToC(f):
    fLocal = float(f)
    cOut = (fLocal - 32) * (5/9)
    print("Input: ", fLocal , " farenheit. Out: ", cOut, " celsius")

# Instead of cluttering __main__, this function calls to get the user's input 
# and use it as an argument for a function
    #@args: NONE
    #@return: float, int
def getUserInputAsReturn():
    userInput = eval(input("Enter a number: "))

    return userInput

# For seperation within program instances, create defined whitespace lines.
def whiteSpace(amount):
    localAmount = amount

    for i in range(amount):
        print("")

# Given two numbers, compute the average (float, int) or (mix)
def compTheAvg():
    print("Hello and welcome!")
    userInputScore1, userInputScore2, userInputScore3 = eval(input("Enter three exam scores seperated by a comma: "))
    print("You entered the first score of: ", userInputScore1, " and the second score of: ", userInputScore2, " and the third score of:", userInputScore3)
    print("Average score is: ", (userInputScore1 + userInputScore2 + userInputScore3) / 3)

#----------------------
if __name__ == "__main__":
    #Code goes here
    whiteSpace(5)
    print("Hello!")
    compTheAvg()