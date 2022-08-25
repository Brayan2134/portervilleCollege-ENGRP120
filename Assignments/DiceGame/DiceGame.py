import random
from DiceGameExternalFunc import *

userRoll = []
computerRoll = []

# Change the numbers of index depending on which ones user wanted
def userChangeNums(userRoll, diceSide):
    print("\nAwesome! Look at the numbers you rolled.")
    print("For each of the numbers, tell me which ones you wish to re-roll!\n")

    reRollKeys = input("[-]For Change, [+] for keep.")

    # Ask user to see which numbers they want to re-roll
    while True:
        # Check to see if every index in userRoll[] has a response
        if (len(reRollKeys) != len(userRoll)):
            print("Sorry! You made a bad input, let's try again (Maybe you forgot about one index?)")
            reRollKeys = input("[-]For Change, [+] for keep: ")
            print("")
            continue

        # CHeck to see if every response has a valid input
        for i in range(0, (len(reRollKeys))):
            if (reRollKeys[i] == "-") or (reRollKeys[i] == "+"):
                print("Evaluating.....")
            
            else:
                print("Sorry! You made a bad input (maybe you pressed a wrong button on your keyboard?")
                reRollKeys = input("[-]For Change, [+] for keep: ")
                print("")
            break

        # Everything is valid! Continue with program
        break

    # For each index, if user chose to change number, change it!
    for i in range(0, len(userRoll)):
        if (reRollKeys[i] == "-"):
            userRoll[i] = random.randint(0, diceSide)


# Roll the users numbers based on given conditions
def userRoll2(diceAmt, diceSide):
    total = 0

    # Initial roll
    for i in range(0, diceAmt, 1):
        discreteNum = random.randint(0, diceSide)
        userRoll.append(discreteNum)
        total = total + discreteNum
    
    # Print results
    print("\nInitial Roll: ", userRoll)

    userChangeNums(userRoll, diceSide)

    print("Final Roll: ", userRoll)

    return total

# See who has the higher total score!
def winnerIs(userTotal, compTotal):
    print("Your total sum: ", userTotal, "\n Computers Total Sum: ", compTotal)

    # Who wins?
    if (userTotal > compTotal):
        print("You win! Sheesh, because imagine losing to a computer how embarrasing...")
    if (compTotal > userTotal):
        print("YOU LOST HAHA IMAGINE!! BE BETTER NEXT TIMEXZZADFQWELKJFW")
    if (compTotal == userTotal):
        print("You tie! What are the odds lol")


# Main function to see how game runs!
def main():
    compTotal = 0
    userTotal = 0

    # Welcome User
    print("\n Welcome!\n Let's play a game. You're already running this program so lets have fun!!!!\n")

    # Define boundaries
    diceSide = eval(input("Enter number sided die: "))
    
    diceAmt = eval(input("How many dice would you like to roll?: "))

    # User rolls their numbers
    userTotal = userRoll2(diceAmt, diceSide)

    # COmputer rolls their numbers
    compTotal = rollForComp(diceAmt, diceSide, compTotal, computerRoll)

    # Determine winner
    winnerIs(userTotal, compTotal)


if __name__ == "__main__":
    main()