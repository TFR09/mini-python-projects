import random

def game():
    secretLength = 5
    secret = ''
    for i in range(secretLength):
        secret += str(random.randint(0,9))
        
    prompt = 'Guess the secret ' + str(secretLength) + ' digit number: '
    guess = input(prompt)
    if len(guess) == secretLength:
        for i in range(0,secretLength):
            if guess[i] == secret[i]:
                print('Y',end = '')
            elif guess[i] > secret[i]:
                print('H',end = '')
            elif guess[i] < secret[i]:
                print('L',end = '')  
            else:
                print('N',end = '')
    else:
        print('Wrong number of digits!')

    #delete the line below in real game play
    #print('\nThe secret number was ', secret)

if __name__ == "__main__":
    game()