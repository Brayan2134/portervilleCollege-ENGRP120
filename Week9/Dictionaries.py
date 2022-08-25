"""
    Name: Quevedo Ramos, Brayan

    Purpose: Learning about Dictionaries in Python
"""

def main():

    # Key: Value
    # Value must be: list, dict, string

    firstDictionary = {
        'This is a Key': 'Values',
        'Second Key': 'Second Value',
        'Hello': 'Password'
    }

    emptyDict = {}


    # Aceess Dict Value
    print(firstDictionary.get('Hello')) # Call Dict to retrieve specific Key
    print(firstDictionary.get("Value That doesn't exist")) # IF Key doesn't exist, it shall return NONE

    # Append To Dict
    firstDictionary["My name Is: "] = "BRAYANNNN"

    print(firstDictionary)

    # Modify Value
    firstDictionary['Second Key'] = 'I DONT KNOW WHAT TO SAY'

    # Delete Key and Value
    del firstDictionary["Hello"]

    print(firstDictionary)

    favLangs = {
        "Brayan Quevedo Ramos" : "C++",
        "Mekai" : "Python",
        "Angel" : "Java",
        "Daniel" : "Python",
        "Beth" : "MATLAB",
        "Fernando" : "Java"
    }

    # Print every Key in dic favLangs
    for hello in favLangs.values():
        print(hello.title())

    sampleArrayKey = ["Brayan Quevedo Ramos", "Fernando"]

    for hello in favLangs.keys():
        if hello in sampleArrayKey:
            print("\n",hello)


    # print nested (FavLangs wrapped inside of aliens)
    aliens = [favLangs]
    for alien in aliens:
        print(alien)


if __name__ == "__main__":
    main()