def midpoint(p1, p2):
    x = (p1[0]+p2[0]) / 2
    y = (p1[1]+p2[1]) / 2
    mid = (x,y)
    return mid

if __name__ == "__main__":
    mid = midpoint((1,2), (7,8))
    print("The midpoint of (1,2) and (7,8) is", mid)
  