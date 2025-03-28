def isLetter(weight, length, width, depth):
  allow = (weight <= 100) and (length <= 240 and length >= 90) and (width <= 165 and width >= 90) and (length >= 140 or width >= 140) and (depth <= 5)

  return allow
  
def isSmallParcel(weight, length, width, depth):
  allow = (weight <= 2000) and ((length + width + depth) <= 90) and (length <= 60) and (width <= 60)and (depth <= 60)
  
  return allow
  
def classifyItem(weight, length, width, depth):
  if isLetter(weight, length * 10, width * 10, depth * 10):
    return 1
  elif isSmallParcel(weight, length, width, depth):
    return 2
  else:
    return 0