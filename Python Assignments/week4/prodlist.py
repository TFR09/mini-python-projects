def prodlist(numList):
  if len(numList) == 0:
    return 1
  else:
    prod = numList[0]
    for i in range(len(numList) - 1):
      prod *= numList[i + 1]
    return prod