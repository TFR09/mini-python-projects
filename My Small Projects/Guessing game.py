from random import randint as ri

print('what is your name?')
name = input()
print('Hello', name, 'lets play a guessing game where you have to guess a number I choose between 1 and 9')
print('Ok lets start.Btw you have only 4 guesses')

snum = ri(1,9)

for guess in range(5):
    print("Choose a number from 1 to 9")
    num = input()
    if int(num) < int(snum):
        print(num ,'is too small')  
    elif int(num) > int(snum):
        print(num ,'is too big')
    elif int(num) == int(snum):
        print('Correct guess but i\'m sure its a fluke')
        break

if int(num) != int(snum):
    print('The correct number was', snum)
    print('You Big Noob')

print('thanks for playing')

    
