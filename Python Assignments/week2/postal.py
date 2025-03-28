def postal():
    weight = int(input("Enter weight(g): "))
    length = int(input("Enter length(cm):"))
    diameter = int(input("Enter diameter(cm):"))

    yes = (weight <= 2000) and (length <= 90) and (length + (2* diameter)<= 104)

    if yes:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    postal()