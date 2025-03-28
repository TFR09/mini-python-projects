def isLetter(weight, length, width, depth):
  allow = (weight <= 100) and (length <= 240 and length >= 90) and (width <= 165 and width >= 90) and (length >= 140 or width >= 140) and (depth <= 5)

  return allow