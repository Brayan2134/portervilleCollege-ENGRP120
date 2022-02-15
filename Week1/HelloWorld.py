#This is a commment

"""
    While this isn't quite the correct syntax,
    one of the beautiful things about Python
    is that you can use triple quotes to
    create a multi-line comment
"""
#Introduction
print("Hello world")
print("This is a test")

#Declaring vars
dummyVar = "Brayan Quevedo Ramos"
veryCoolArg = "This is an argument"

#displaying vars
print(dummyVar)

#Print more than argument
print("This is a first argument", veryCoolArg)

#Python operations

#a + b
print(5 + 3)

#a - b
print(4 - 1)

#multiplication
print(33 * 420)

#Division
print(420/69)

#MOD
print(15 % 4)

print()
print()
print()

#Define a function
def thisIsAFunction():
    print("This will be displayed if there is a call for a function")


def getAName():
    userName = input("Plase Enter your name:")
    print(userName)

def getTempF(celsius):
    faren = (celsius * (9/5) + 32)
    print("Celsius: ", celsius, " is the same as: ", faren, " farenheit")


sampleArray = ['1', '2', '3', '4']

#-----------------------------------------------------------------
#thisIsAFunction() #Call For function
#getAName()
#getTempF(3)
