from random import*
import time
while True:
    print('Do you want to play?(yes/no)')
    ans = input()
    if ans.lower() == 'yes':
        print('rock(r), paper(p) or scissors(s)?')
        player = input()

        chosen = randint(1,3)
        
        if chosen == 1:
            computer = 'r'
        elif chosen == 2:
            computer = 's'
        elif chosen == 3:
            computer = 'p'

        time.sleep(2)
        
        print(player,'vs', computer)
        # rock beats scissors
        # paper beats rock
        # scissors beats paper
        if player == computer:
            print('DRAW')
        elif player == 'r' and computer == 's' or player == 's' and computer == 'p' or  player == 'p' and computer == 'r':
            print('You win!')
        elif player == 's' and computer == 'r' or player == 'p' and computer == 's' or  player == 'r' and computer == 'p':
            print('Computer wins!')

    else:
        print('Wow ok then.')

    print('Goodbye')
