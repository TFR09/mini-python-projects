def beans():
    blackB = int(input("Enter number of black beans in can: "))
    whiteB = int(input("Enter number of white beans in can: "))

    WW = (whiteB >= 2)
    BB = (blackB >= 2)
    BW = (blackB >= 1) and (whiteB >= 1)
    
    print("Allowed operations:")
    if WW:
        print("WW pick out two white beans")
    if BB:
        print("BB pick out two black beans")
    if BW:
        print("BW pick out one white and one black bean")

    option = input("Enter your option: ")

    if option == "BB":
        blackB -= 2
        blackB += 1
    elif option == "WW":
        whiteB -= 2
        blackB += 1
    elif option == "BW":
        blackB -= 1
    else:
        print("Operation not allowed")

    print(blackB," black beans")
    print(whiteB," white beans")


if __name__ == "__main__":
    beans()