import random

def number():
    for i in range(10):
        x = random.randint(0, 99)
        print("The number picked was ", x)


if __name__ =="__main__":
    number()