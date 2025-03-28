def isSmallParcel(weight, length, width, depth):
  allow = (weight <= 2000) and ((length + width + depth) <= 90) and (length <= 60) and (width <= 60)and (depth <= 60)
  
  return allow