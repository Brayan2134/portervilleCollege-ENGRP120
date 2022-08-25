from curses import window
from Graphics import *

def main():
    windows = GraphWin("Battle", 1000, 1000)

    pokeBallOutline = Circle(Point(500,500), 50)
    pokeBallOutline.draw(windows)

    pokeBallInner = Circle(Point(500,500),10)
    pokeBallInner.draw(windows)

    for i in range(0,360):
        pos1 = Point((i + 450),(i + 500))
        ps2 = Point((550 - i),(500 - i))
        leftLine = Line(pos1, ps2)
        leftLine.draw(windows)
main()

