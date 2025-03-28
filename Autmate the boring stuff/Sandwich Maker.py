from pyinputplus import *

prices = {'wheat': 0.80, 'white': 0.60, 'sourdough': 1.10, 'chicken': 2.10, 'turkey': 1.75, 'ham': 1.90, 'tofu': 2.50,
          'cheddar': 1.40, 'swiss': 1.50 ,'mozzarella': 1.90}

price = 0

input("Welcome to this sandwich maker app. Here you can make your own choice of sandwhiches.\nTo start the program press any key")

bread = inputMenu(['wheat', 'white', 'sourdough'],numbered = True,prompt = 'Please choose a bread type.\n')
price += prices[bread]

meat = inputMenu(['chicken', 'turkey', 'ham', 'tofu'],numbered = True, prompt = 'Please choose your preferred protein.\n')
price += prices[meat]

cheese = inputYesNo(prompt = 'Would you lIke some cheese?\n')
if cheese == 'yes':
    cheesetype = inputMenu(['cheddar', 'swiss', 'mozzarella'],numbered = True, prompt = 'Please choose your cheese.\n')
    price += prices[cheesetype]

addons = inputYesNo('Would you like mayo, mustard, lettuce or tomato?\n')
if addons == 'yes':
    price += 0.5

sandwiches = inputInt("How many sandwiches do you want?\n", min = 1)
total = price * sandwiches
print("Your total price is ${:.2f}. Thank you".format(total))
