def year():
    year = int(input("Enter year: "))
  
    common = ((year % 400 != 0) and (year % 100 == 0))

    if (year % 4 != 0) or common:
        print("Common year")
    else:
        print("Leap year")


if __name__ == "__main__":
    year()