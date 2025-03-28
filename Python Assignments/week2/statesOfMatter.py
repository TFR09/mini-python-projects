def state():
    temp = float(input("Enter temperature in Celcius: "))
  
    if temp >= 100:
        print("gaseous")
    elif temp <= 0:
        print("solid")
    else:
        print("liquid")


if __name__ == "__main__":
    state()