from Graphics import *
import time

def main():
    win = GraphWin("Sample", 1000, 1000)

    point = Point(50,60)
    point.draw(win)
    
    time.sleep(1)

    sally = Point(100,100)
    sally.draw(win)
    
    time.sleep(1)

    hello = Point(0,0)
    hello.draw(win)

    for i in range(0,100):
        time.sleep(0.1)
        hello.move(1, 1)

    cirles = Circle(sally, 100)
    cirles.draw(win)

    time.sleep(1)

    createText = Text(point, "Hello My Nmae is:")

    createText.draw(win)
    time.sleep(5)

if __name__ == "__main__":
    main()