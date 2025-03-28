def eggs():    
    eggs = int(input("Number of eggs: "))

    boxes = int(eggs // 6)
    remain = int(eggs % 6)
    print("You can make", boxes, "boxes with", remain, "eggs left over")

if __name__ == "__main__":
    eggs()