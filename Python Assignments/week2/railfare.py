def fare():
    age = int(input("Enter age: "))
    agegrp = (age < 16) or (age > 59)
    
    if agegrp:
        print("Fare is 120")
    else:
        print("Fare is 150")


if __name__ == "__main__":
    fare()