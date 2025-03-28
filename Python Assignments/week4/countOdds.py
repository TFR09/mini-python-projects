def countOdds(numlist):
  counter = 0
  for i in range(len(numlist)):
    if (numlist[i] % 2 == 1):
      counter += 1
  return counter