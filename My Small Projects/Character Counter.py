from pprint import *


def counter():
    print("Enter a message!")
    message = input()

    count = {}

    for char in message.lower():
        count.setdefault(char, 0)
        count[char] += 1

    pprint(count)

    input()

if __name__ == "__main__":
    counter()
