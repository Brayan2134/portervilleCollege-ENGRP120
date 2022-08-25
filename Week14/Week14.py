message = input("Enter text (make it fun)?: ")
encMessageArr = []
import random

def main():
    for i in range(0, len(message)):
        encMessageArr.insert(i, ord(message[i]))
        encMessageArr[i] = (encMessageArr[i] * 69420) ** 2
        print(chr(ord(message[i]) * random.randint(1,200)))

    decode()

def decode():
    decMessageArr = []
    for i in range(0, len(message)):
        decMessageArr.insert(i, int((encMessageArr[i] ** (1/2)) / 69420))
        print(chr(decMessageArr[i]))
    print(decMessageArr)

main()