from itertools import count


def hellWorld():
    print("Hello")


#Say hello to someone
#args: str
def sayHello(str):
    print("Hello, ", str)



def mathFunc(inputFloat):
    output = 3 * (inputFloat) + 5
    print("Output is: ", output)


#
    #@args: countTo (int), userNumber (float)
        #countTo (int): number of cycles user wishes to repeat
        #userNumber (float): input for ChaosTheory equation
#

def chaosTheory(countTo, localUser):
    print("This program illustrates a chaotic function")
    i = 0
    while (i < countTo):
        i = i + 1
        localUser = 2.0 * localUser * (1 - localUser)
        print(localUser)

#----------------------

if __name__ == "__main__":
    userNumber = eval(input("Enter a number from 0-x: "))
    userCount = eval(input("Enter repititions: "))
    chaosTheory(userCount, userNumber)