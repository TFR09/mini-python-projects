def cuboid():
    print('Please enter the width')
    w = float(input())
    print('Please enter the height')
    h = float(input())
    print('Please enter the depth')
    d = float(input())

    volume = w * d * h
    print("Volume is ", volume)

if __name__ == "__main__":
    cuboid()