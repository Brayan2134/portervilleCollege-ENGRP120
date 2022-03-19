vowels = ['a', 'e', 'i', 'o', 'u']

def main():
    print("Hello!")
    userName = input("What's your name?: ")
    userName = userName.lower()

    doesUserHaveVowel = checkIfVowel(userName) # If user did have a vowel as first letter, return True

    # If user does have vowel, move first letter to last and add ay
    if (doesUserHaveVowel == True):
        userName = userHasConstant(userName)
    # If user soes have Vowel, just add 'way' to it!
    elif (doesUserHaveVowel == False):
        userName = userHasVowel(userName)
    else:
        print("You aren't supposed to be here")
    
    print(userName)


# Check if the user has vowel as first letter in str
def checkIfVowel(userText):
    userVowel = False
    # Check first letter of userName to see if it has a vowel
    for i in range(0, len(vowels), 1):
        if (userText[0] == vowels[i]):
            userVowel = True
    return userVowel
    

# Take the user text, move first letter to end, and add 'ay' to it.
def userHasConstant(userText):
    localUserText = userText[0] # Remove line if Python doesn't unconcatinate userText[1:] when called 
    userText = userText[1:] + localUserText + "ay" 
    return userText

# IF user has vowel, add 'way' to end
def userHasVowel(userText):
    userText = userText + "way"
    return userText

if __name__ == "__main__":
    main()