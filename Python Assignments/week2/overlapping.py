def overlap():
    startA = int(input("Enter start hour for event A: "))
    durA = int(input("Enter duration for event A: "))
    startB = int(input("Enter start hour for event B: "))
    durB = int(input("Enter duration for event B: "))

    endA = startA + durA
    endB = startB + durB
    
    notoverlap = (endA <= startB) or (endB <= startA)
    
    if notoverlap:
        print("not overlap")
    else:
        print("overlap")


if __name__ == "__main__":
    overlap()