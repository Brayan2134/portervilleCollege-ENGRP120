a = 6
#print(type(a))
#print(id(a)) # Memory Address

b = 6
#print(type(b))
#print(id(b)) # Memory Address

dogs = "this is a string that is lowercase, but when .title() is used, this should be a cap"
#print(dogs.title())

#print(dogs * 3) # Print str 3x

helloWorld = "Hello World"
#print(helloWorld.lower())
#print(helloWorld.upper())
#print(len(helloWorld))
#print(helloWorld.strip("Hell"))


"""
    Name: Brayan Quevedo Ramos
    Initial Commit Date: 16, Feb 2022

    Purpose: To work with String[arg] methods
"""

givenQuote = '"I am running away from my responsibilities. And it feels good."'
givenQuoteAuthor = "Michael Scott"

def showQuote():
    print(f"{givenQuote.upper()} -- {givenQuoteAuthor.center(200)}")

#showQuote()

sampleArray = [] #Array Indexing is 0

for i in range(0, 10, 1):
    sampleArray.append("Hello")

#print(sampleArray)

multiDimensionalArray = [] # Array will be [x,y]

for i in range(0,10,1): # Define [x, ] in array
    for j in range(0,10,1): # Define [ ,y]
        multiDimensionalArray.append([i,j]) # Append [x,y] in array

#print(multiDimensionalArray)

multiDimensionalArray.extend(sampleArray)

#print(multiDimensionalArray)

pizzaName = [["peporoni with", " mushrooms"], ["peporoni with", " black olives"], ["peporoni with", " garlic and", " pineapple"]]

#for pizzaType in range (0, len(pizzaName), 1):
    #print(f"The Pizzas I tend to buy the most are: {pizzaName[pizzaType]}") # how to remove brackets?
#print(f"Therefore, I have {len(pizzaName)} favorite pizzas")

numbersCool = []
for insertThing in range (0, 33, 3):
    numbersCool.append(insertThing ** 3)

print(numbersCool) # Sir this is a wendy's