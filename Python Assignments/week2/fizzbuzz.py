def fizzbuzz():
    num = int(input("Enter an integer: "))

    if (num % 3 == 0) and (num % 5 == 0):
        print("Fizz Buzz")
    elif (num % 3 == 0):
        print("Fizz")  
    elif (num % 5 == 0):
        print("Buzz")
    else:
        print(num)


if __name__ == "__main__":
    fizzbuzz()