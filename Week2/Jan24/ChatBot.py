#
    #Date (Original): Mon, Jan 24 2022
    #Author: Brayan Quevedo Ramos
    #Co-Author(s): N/A

    #Purpose: General pupose chatbot

    #Remarks:
#

#IMPORTS
import datetime
import random
import math
#--------------------

#Main function ran
def main():
    aiIntroduction()

"""
    All methods listed below are under the class name "AI"

    ClassName has not been created yet.
"""


# Simple introduction @noParams
def aiIntroduction():
    print("Hello! My name is Steve the chat bot.")
    userName = input("What's your name? ")
    print("Hello, " + userName)
    
    howUserFeels()
    dateTime()


# Non-int @noParams
def howUserFeels():
    print("Some days are rough.")
    userSent = input("How are you feeling? ")
    userContSent = input("Why do you feel this way? ")
    print("Well no matter the case, I hope you have an excellent day! ")



# GetDateTime @noParams
# NOTE: Read documentation on datetime.method (obj, inst)
def dateTime():
    print()
    print("The current date is: ", datetime.datetime(2022, 1, 24))

    guessBotAge()


def guessBotAge():
    botAge = random.randint(1, 1000)
    print()
    userGuess = input("Can you guess my age? ")

    if (userGuess == botAge):
        print("Correct! You guessed my name correctly!")
    else:
        print("Sorry, you didn't guess the correct answer.")
        print("You guessed that my age was: " , userGuess, " when my real age was: ", botAge)
        ageDiffBWUserAndBot = abs(botAge - int(userGuess))
        print("You were only off by ", ageDiffBWUserAndBot, " years!")

    favFood()


def closeOff():
    print()
    print("Well, this concludes our conversation. Until next time!")


def favFood():
    userFavFood = input("What's your fav food? ")
    print("No way? same too! Mine's also ", userFavFood)

    closeOff()

#-------------------------------

#Init .py as script
if __name__ == "__main__":
    main()