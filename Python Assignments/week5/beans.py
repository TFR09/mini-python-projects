def doNextOp(state,capA,capB):
  A = state[0]
  B = state[1]
  if A == 0:
    state[0] = capA
    return "FA"   
  elif B == capB:
    state[1] = 0
    return "EB"
  else:
    if ((capB - B) >= A):
      state[0] = 0
      state[1] += A
    else:
      state[0] -= (capB - B)
      state[1] = capB
    return "AB"

def main():
  capA = int(input("Enter capacity of jug A: "))
  capB = int(input("Enter capacity of jug B: "))
  vol = int(input("Enter desired volume of water: "))

  state = [0,0]
  i = 0
  desired = (vol == state[0]) or (vol == state[1]) or (i == (capA+capB))
  
  while not desired:
    op = doNextOp(state,capA,capB)
    if op == "AB":
      print("AB - Transfer as much water as possible from jug A to jug B")
    elif op == "FA":
      print("FA - Fill jug A")
    else:
      print("EB - Empty jug B")
    print("There are now",state[0],"litres in jug A and",state[1],"in jug B")
    i += 1
    desired = (vol == state[0]) or (vol == state[1]) or (i == (capA+capB))
  
  if state[0] == vol:
    print("The desired amount is in jug A")
  elif state[1] == vol:
    print("The desired amount is in jug B")
  else:
    print("Couldn't get desired volume")

if __name__ == "__main__":
  main()