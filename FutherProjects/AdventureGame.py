"""
    Name: Brayan Quevedo Rmaos
    Initial Commit Date: 2, March 2022

    Purpose:
"""

import random
import time
import AdventureGameFunc

# A Trainer class for user and opponents
class Trainer:
    def __init__ (self, name, pokemon, items):
        self.name = name
        self.pokemon = pokemon
        self.items = items

    def getName(self):
        return self.name

    def pokemon(self):
        return self.pokemon

bagItems = [] # Bag of items in Pokemon

# Current Pokemon user has
trainerPokemon = ["Luxray", 20, "Electric", "Thundershock", 5]# Name, Health, Type, Moves

# Introduction to game
def introduction():
    print("****************")
    print("Hello!")
    print("Welcome to the pirated version of Pokemon!")
    print("*****************")

# Selection menu so user can do what they wish in their adventure
def menuSelect(userOption):
    userOption = userOption.lower()

    if (userOption == "a" or userOption == "b" or userOption == "c"):
        return True
    else:
        return False

# Check to see if you can run away from an encounter
def checkIfCanRun():
    numCantRun = random.randint(0,100)

    if numCantRun == 50:
        print("Sorry! You couldn't get away...")
    else:
        print("You got away!")

# Check the user's bags
def checkInventory():
    lenInventory = len(bagItems)

    if lenInventory == 0:
        print("You have no items!")
    
    storyMenu()


# Check the user pokemons moves
def battleMoves(userMoves):

    moves = len(trainerPokemon[3])
    if moves == 0:
        print("You have no moves left!")
        print("You used: Struggle")

    else:
        print("Your current moves are: ", trainerPokemon[3])

# Battle against trainer max
def battle(userPokemon, trainerPokemon):
    localPokemon = trainerPokemon[0] # Get the pokemon user will use
    localHealth = trainerPokemon[1] # Get the health of the pokemon
    localMoves = str(trainerPokemon[3]) # Get the moves the pokemon can use

    oppositionPokemon = userPokemon[0] # Get Trainer Max's Pokemon
    oppositionHealth = userPokemon[1] # Get Trainer Max's Pokemon's Health
    oppositionPokemonMove = userPokemon[3]

    # Fight until one pokemon dies.
    while (localHealth > 0) & (oppositionHealth > 0):
        print("")
        time.sleep(2)
        print(oppositionPokemon, " has ", oppositionHealth, " health")
        time.sleep(1)
        print(localPokemon, " has ", localHealth, " health")

        userChooseMove = input("Type which move to use: ")

        if userChooseMove == localMoves:
            print("")
            print("Cool! ", localPokemon, " used: ", localMoves)
            oppositionHealth = oppositionHealth - trainerPokemon[4]
        else:
            print("")
            print("Oops, you chose an invalid answer. Because of this, you lost your turn...")
            print("Make sure to type your move exactly as shown!")

        time.sleep(3)

        print("Trainer Max's ", oppositionPokemon, " used: ", oppositionPokemonMove)
        localHealth = localHealth - userPokemon[4]

    if (localHealth > oppositionHealth):
        print("You have sucsessfully beaten Trainer Max!")
    else:
        AdventureGameFunc.loseScreen()

# Create trainer max to fight against
def maxTheTrainer():
    trainerMaxPokemon = ["Squirtle", 10, "Water", "Tackle", 3] # Name, Health, Type, Moves
    trainerMax = Trainer("Max", trainerMaxPokemon, "None")

    print("")
    print("******************")
    print("MUAH HAH HA")
    print("We have met eyes while you were on route 207. This means we must battle!")
    userGetsTrainerName = input("What do you think my name is?: ")

    localName = str(trainerMax.getName())
    if (userGetsTrainerName == localName):
        print("WHAT? NO WAY? How do you... know my name.. Carry on I gues.s..")

    else:
        time.sleep(2)
        print("I knew you couldn't handle me!")
        time.sleep(2)
        print("Let's battle!!!!")
        time.sleep(2)
        print("(Pokemon gen 4 music starts)")
        time.sleep(2)
        print("\n","Trainer ",trainerMax.getName(), "has sent out: ", trainerMaxPokemon[0])
        battleMoves(trainerPokemon)
        battle(trainerMaxPokemon, trainerPokemon)

# The menu where user selects what they wish to do!
def storyMenu():
    correctInput = False
    while (correctInput == False):
        print("\n")
        print("What would you like to do?")
        print("A: Run Away!")
        print("B: Check Inventory")
        print("C: FIGHT!")
        userOption = input("What's your choice?: ")
        print("\n")
        correctInput = menuSelect(userOption)

        if (correctInput == True):
            break

    if userOption == 'a':
        checkIfCanRun()
    if userOption == 'b':
        checkInventory()
    if userOption == 'c':
        maxTheTrainer()



def main():
    introduction()
    storyMenu()

#---------------------------------------
if __name__ == "__main__":
    main()