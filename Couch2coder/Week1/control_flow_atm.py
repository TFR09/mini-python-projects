# Account info
balance = 500
pin = 7168

user = int(input("Enter your pin > "))

if user != pin:
    print("PIN is incorrect")
else:
    print("Your balance is $", balance)

    action = input("Do you want to withdraw or deposit? > ").lower()
    amount = int(input(f"How much would you like to {action}? > "))

    if action == "withdraw":
        balance -= amount
    elif action == "deposit":
        balance += amount
    else:
        print("Invalid action!")

    print("Your updated balance is $",balance)
