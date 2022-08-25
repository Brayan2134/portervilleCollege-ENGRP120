import time
from Graphics import *

def loseScreen():
    win = GraphWin("DEATH SCREEN", 500,116)
    point1 = Point(190,0)
    image1 = Image(point1, "/Users/brayan/Documents/School/Porterville Community College/Classes/Spring '22/ENGRP120 - Introduction to Programming Concepts and Methodologies for Engineers/portervilleCollege-ENGRP120/FutherProjects/west.png")
    image1.draw(win)
    print("Wait what?")
    time.sleep(1)
    print("Everything went black!")
    time.sleep(2)
    print("You fainted.")
    time.sleep(1)
    print("You died.")


def introScreen():
    win = GraphWin("Introduction", 1500,800)
    point1 = Point(700,350)
    image1 = Image(point1, "/Users/brayan/Documents/School/Porterville Community College/Classes/Spring '22/ENGRP120 - Introduction to Programming Concepts and Methodologies for Engineers/portervilleCollege-ENGRP120/FutherProjects/intro.png")
    image1.draw(win)
    time.sleep(5)
    win.close()

def battleScreen():
    win = GraphWin("BATTLE", 1500,800)
    point1 = Point(700,350)
    image1 = Image(point1, "/Users/brayan/Documents/School/Porterville Community College/Classes/Spring '22/ENGRP120 - Introduction to Programming Concepts and Methodologies for Engineers/portervilleCollege-ENGRP120/FutherProjects/battle.png")
    image1.draw(win)
    time.sleep(5)
    win.close()

loseScreen()