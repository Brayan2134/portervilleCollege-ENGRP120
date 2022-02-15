"""
    Name: Brayan Quevedo Ramos
    Initial Commit Date: 3, Feb, 2022

    Program: What's For Sale?

    Purpose: First look into Object-Orientated programming by allowing user to essentially being a 'Python Version' of McDonalds.
             While the entire menu won't be replicated, some of the menu will be!

    Need to work on: Better system to add and subtract class elements so program can scale inf.

    Notes: userOrder[] and userTotal[] must be parallel arrays!
"""

#-------------Class variables-----------------
# CLASS MenuItem
# @CLASSargs: self (self), itemName (str), itemPrice (float)
# @CLASSspecial: Used to create all of the menu items for the Mcdonalds restarunt.
# @note: 
class MenuItem:
    def __init__ (self, itemName, itemPrice, itemQuantity, itemNumber):
        self.itemName = itemName
        self.itemPrice = itemPrice
        self.itemQuantity = itemQuantity
        self.itemNumber = itemNumber
    
    def print(self):
        print(self.itemName, " ", self.itemPrice, " ", self.itemQuantity, " ", self.itemNumber)

    def getName(self):
        return self.itemName

    def getPrice(self):
        return self.itemPrice
#-------------End Class Variables-------------

#-------------Global variables-----------------
userOrder = [] # How many menuItems (str) have been allocated
userTotal = [] # Get itemPrice (float) for same index number of userOrder

cheeseburger = MenuItem("CheeseBurger", 1.99, 1, 100)
hamburger = MenuItem("Hamburger", 1.49, 1, 101)
chickenburger = MenuItem("McChicken", 2.49, 1, 102)
chickenNuggets = MenuItem("Chicken Nuggets (10 piece)", 4.99, 1, 103)
eggMcMuffin = MenuItem("EggMcMuffin", 3.50, 1, 104)

#-------------End Global Variables-------------

#-------------Function: introduction()---------
# @args: none
# @special: will be called. Should only be seen once per execution.
def introduction():
    print("")
    print("")
    print("******************************")
    print("Hello and welcome to McDonalds!")

    mainMenu()


#-------------Function: mainMenu()------------
# @args: none
# @special: will be called by some function to continue loop.
# @timecomp: O(n)
#           - n: how many times user failed to select correct option
def mainMenu():
    print("How may I take your order?")
    print("[1]: Show Menu")
    print("[2]: Check Cart")
    print("[3]: Checkout")

    userMoveOn = False
    userChoice = 0

    while (userMoveOn == False):
        userChoice = eval(input("Please select an option: "))
        userMoveOn = checkUserAnswer(userChoice)

    caseSwitchForMainMenu(userChoice)
        

#-------------Function: checkUserAnswer()---------
# @args: userChoice (int)
# @special: Can only be called by mainMenu()
#           - Checks arg userChoice to see if correct input was made on the mainMenu() function
# @timecomp: O(3)
#           - 3: Worst case scnario where for the if statement does 3 checks to see if user 
#                selected correct menu option!
def checkUserAnswer(userChoice):
    localUserChoice = userChoice
    if (localUserChoice == 1 or localUserChoice == 2 or localUserChoice == 3):
        # user has sucsessfully made a choice
        return True
    else:
        print("Sorry! I didn't understand that can you try again?")
        return False


#-------------Function: caseSwitchForMainMenu()-----
# @args: valueChosen (int)
# @special: Can only be called by mainMenu()
#           - Used to redirect user to one of three function [provided by mainMenu]
#           to the function that does what user wanted to do!
# @timecomp: O(3)
#           - 3: Worst case scnario where user wanted 3rd option from mainMenu()
#                therefore alg must make 3 comparisons.
def caseSwitchForMainMenu(valueChosen):
    if valueChosen == 1:
        showMenu()
    elif valueChosen == 2:
        checkCart()
    elif valueChosen == 3:
        checkOut()
    else:
        print("Whoops you're not supposed to be here")



#-------------Function: showMenu()------------------
# @args: none
# @special: Can only be called by caseSwitchForMainMenu(valueChosen)
#           - Used to show what current menu is
#           - Menu is defined in globals via objects!
def showMenu():
    print("")
    print("Our Menu is: [name], [price], [quantity], [item number]")
    print("")
    cheeseburger.print()
    hamburger.print()
    chickenburger.print()
    chickenNuggets.print()
    eggMcMuffin.print()

    addFood()

    mainMenu()


#-------------Function: addFood()-----------------
# @args: none
# @special: Can only be called by showMenu()
#           - Used so user can select which item to pick (via self.itemNumber)
#             and add that to global arrays for keeping track of order!
# @timecomp: O(n + 4)
#           - NEED TO WORK ON ALG.
#           - n + 4: Worst case is that user orders infinite items of the given elements (if inside while)
def addFood():
    userChoseMenuItem = eval(input("Please select a menu item (use item number): "))
    print(userChoseMenuItem)

    i = 0
    if userChoseMenuItem == 100:
        addToArray = eval(input("How many Cheeseburger's would you like?: "))
        print(addToArray)

        while (i < int(addToArray)):
            userOrder.append(cheeseburger.getName())
            userTotal.append(cheeseburger.getPrice())
            i = i + 1

    if userChoseMenuItem == 101:
        addToArray = eval(input("How many Hamburger's would you like?: "))
        print(addToArray)

        while (i < int(addToArray)):
            userOrder.append(hamburger.getName())
            userTotal.append(hamburger.getPrice())
            i = i + 1

    if userChoseMenuItem == 102:
        addToArray = eval(input("How many McChicken's would you like?: "))
        print(addToArray)

        while (i < int(addToArray)):
            userOrder.append(chickenburger.getName())
            userTotal.append(chickenburger.getPrice())
            i = i + 1

    if userChoseMenuItem == 103:
        addToArray = eval(input("How many Chicken Nuggets's would you like?: "))
        print(addToArray)

        while (i < int(addToArray)):
            userOrder.append(chickenNuggets.getName())
            userTotal.append(chickenNuggets.getPrice())
            i = i + 1

    if userChoseMenuItem == 104:
        addToArray = eval(input("How many Egg McMuffin's would you like?: "))
        print(addToArray)

        while (i < int(addToArray)):
            userOrder.append(eggMcMuffin.getName())
            userTotal.append(eggMcMuffin.getPrice())
            i = i + 1



#-------------Function: checkCart()-----------------
# @args: none
# @special: Can only be called on by caseSwitchForMainMenu()
#           - Check through array to see what items the user has ordered
def checkCart():
    checkThroughOrder()
    mainMenu()



#-------------Function: checkOut()--------------------
# @args: none
# @special: Can only be called on by caseSwitchForMainMenu()
#           - Check out the customer
#           - Go through userTotal array [0, n] and create recursive function to sum all indexes (in array)
def checkOut():
    print(checkThroughOrder())

    checkOutPrice = 0.0
    i = 0

    while (i < len(userTotal)):
        checkOutPrice = checkOutPrice + userTotal[i]
        i = i + 1

    checkOutPrice = checkOutPrice + (checkOutPrice * 0.0975)
    print("Final price: ", round(checkOutPrice, 2), "$")



#-------------Function: checkThroughOrder()------------
# @args: none
# @special: Go through userOrder[] to see how much of each item there is.
#           - Then print how much of each item has been calculated.
# @timecomp: O(n * 4)
#           - NEED TO WORK ON ALG.
#           - n * 4: Must loop through entire array four times to count how many items there are
def checkThroughOrder():
    strOrder = "You have: "
    amtOf100 = int(userOrder.count(cheeseburger.getName()))
    amtOf101 = int(userOrder.count(hamburger.getName()))
    amtOf102 = int(userOrder.count(chickenburger.getName()))
    amtOf103 = int(userOrder.count(chickenNuggets.getName()))
    amtOf104 = int(userOrder.count(eggMcMuffin.getName()))

    if (amtOf100 > 0):
        strOrder = strOrder + " " + str(amtOf100) + " Cheeseburgers"
    if (amtOf101 > 0):
        strOrder = strOrder + " " + str(amtOf101) + " Hamburgers"
    if (amtOf102 > 0):
        strOrder = strOrder + " " + str(amtOf102) + " McChickens"
    if (amtOf103 > 0):
        strOrder = strOrder + " " + str(amtOf103) + " Chicken Nuggets"
    if (amtOf104 > 0):
        strOrder = strOrder + " " + str(amtOf104) + " Egg McMuffins"

    print(strOrder)

#-------------Function: main()-----------------
# @args: none
# @special: takes global hasUserSeenIntro and converts to true once user has seen 
#           the introduction!
def main():
    introduction()



#-------------------------
if __name__ == "__main__":
    main()