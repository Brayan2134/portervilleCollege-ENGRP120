aliens = []

def initAliens(aliens):
    for alien_number in range(0,30,1):
        new_alien = {
            "Color" : "Green",
            "Points" : 5,
            "Speed" : "Slow",
        }
        aliens.append(new_alien)

def changeAlienSettings(aliens):
    for aliens in aliens[:3]:
        if aliens["Color"] == "Green":
            aliens["Color"] = "Yellow"
            aliens["Speed"] = "Medium"
            aliens["Points"] = 10

        elif aliens["Color"] == "Yellow":
            aliens["Color"] = "Red"
            aliens["Speed"] = "Fast"
            aliens["Points"] = 15
        
        else:
            print("IDK")
def main():

    initAliens(aliens)
    print(aliens[:5])

    changeAlienSettings(aliens)
    print(aliens[:5])


    changeAlienSettings(aliens)
    print(aliens[:5])

if __name__ == "__main__":
    main()