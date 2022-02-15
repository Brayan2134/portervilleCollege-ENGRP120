def main():
    print("Newtons Method!")
    newtonsMethod()

def newtonsMethod():
    x = eval(input("Guess user input: "))
    maxIt = eval(input("Enter max iterations:"))
    for i in range (0, maxIt, 1):
        x = x - (x ** 2 - 8) / (2 * x)
        print(x)

if __name__ == "__main__":
    main()