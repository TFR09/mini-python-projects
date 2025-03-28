import random as r

def bigger():
    numlist = []
    bigger = []
    for i in range(10):
        numlist.append(r.randint(0,99))
    for k in range(len(numlist)):
        if (numlist[k] >= 50):
            bigger.append(numlist[k])

    print("Complete list: ", numlist)
    print("Of which: ",bigger," are >=",50)


if __name__ =="__main__":
    bigger()