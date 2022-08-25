import random

def compChangeEvenNums(diceSide, computerRoll):
    for i in range(0, len(computerRoll)):
        if ((i % 2) == 0):
            computerRoll[i] = random.randint(0, diceSide)
    
    return computerRoll

def compChangeOddNums(diceSide, computerRoll):
    for i in range(0, len(computerRoll)):
        if ((i % 2) == 1):
            computerRoll[i] = random.randint(0, diceSide)
    

def compRandCompleteNums(diceSide, computerRoll):
    for i in range(0, len(computerRoll)):
        computerRoll[i] = random.randint(0, diceSide)

    return computerRoll

def addAllNums(computerRoll):
    compTotal = 0 
    for i in range(0, len(computerRoll)):
        compTotal = compTotal + int(computerRoll[i])
    return compTotal

def changeRandomCompNumbers(diceSide,computerRoll):
    rand = random.randint(0,2)

    if rand == 0:
        compChangeEvenNums(diceSide, computerRoll)

    if rand == 1:
        compChangeOddNums(diceSide, computerRoll)

    if rand == 2:
        compRandCompleteNums(diceSide, computerRoll)

    sumTotal = addAllNums(computerRoll)

    return sumTotal

# Roll computers numbers based on given conditions
def rollForComp(diceAmt, diceSide, compTotal, computerRoll):

    print("\n Now the computer will roll...\n")

    compTotal = 0 
    # Computer uses same boundaries and rolls to create sum
    for i in range(0, diceAmt, 1):
        computerRollNum = random.randint(0, diceSide)
        computerRoll.append(computerRollNum)
    
    compTotal = changeRandomCompNumbers(diceSide, computerRoll)

    print("Computers numbers: ", computerRoll)
    return compTotal